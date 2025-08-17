#!/usr/bin/env python3
"""
🌐💎⚡ LAPTOP-TO-PI TASK OFFLOADING CLIENT (GIGABIT OPTIMIZED) ⚡💎🌐
High-performance client for offloading computational tasks to Pi micro-cloud
"""

from dataclasses import dataclass, asdict
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Callable
import json
import logging
import socket
import threading
import time

from concurrent.futures import ThreadPoolExecutor
import aiohttp
import asyncio
import hashlib
import psutil
import queue
import uuid
@dataclass
class OffloadTask:
    """📋 Task definition for Pi offloading"""
    task_id: str
    task_type: str
    payload: Dict[str, Any]
    priority: str = "normal"
    timeout: int = 30
    retry_count: int = 3
    created_at: str = ""

    def __post_init__(self):
        if not self.created_at:
            self.created_at = datetime.now().isoformat()

@dataclass
class TaskResult:
    """📊 Task execution result"""
    task_id: str
    status: str
    result: Any = None
    error: str = ""
    execution_time: float = 0.0
    pi_node_id: str = ""
    completed_at: str = ""

    def __post_init__(self):
        if not self.completed_at:
            self.completed_at = datetime.now().isoformat()

class GigabitPiOffloadClient:
    """🚀 High-performance Pi task offloading client optimized for Gigabit connection"""

    def __init__(self, pi_ip: str = "192.168.1.200", max_concurrent_tasks: int = 20):
        self.pi_ip = pi_ip
        self.pi_base_url = f"http://{pi_ip}"
        self.max_concurrent_tasks = max_concurrent_tasks

        # High-performance session configuration
        self.connector = aiohttp.TCPConnector(
            limit=100,              # Total connection limit
            limit_per_host=50,      # Per-host connection limit
            ttl_dns_cache=300,      # DNS cache TTL
            use_dns_cache=True,
            keepalive_timeout=60,   # Keep connections alive
            enable_cleanup_closed=True
        )

        # Task management
        self.active_tasks = {}
        self.task_queue = asyncio.Queue(maxsize=100)
        self.results_queue = asyncio.Queue()
        self.task_workers = []

        # Performance metrics
        self.metrics = {
            'tasks_submitted': 0,
            'tasks_completed': 0,
            'tasks_failed': 0,
            'avg_execution_time': 0.0,
            'network_utilization': 0.0,
            'connection_pool_usage': 0
        }

        # Logging setup
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

        # Performance monitoring
        self.performance_monitor = threading.Thread(target=self._monitor_performance, daemon=True)
        self.performance_monitor.start()

    async def __aenter__(self):
        """🔗 Async context manager entry"""
        self.session = aiohttp.ClientSession(
            connector=self.connector,
            timeout=aiohttp.ClientTimeout(total=60, connect=10),
            headers={
                'User-Agent': 'GigabitPiOffloadClient/1.0',
                'Accept': 'application/json',
                'Connection': 'keep-alive'
            }
        )

        # Start task workers
        for i in range(self.max_concurrent_tasks // 2):  # Start with half capacity
            worker = asyncio.create_task(self._task_worker(f"worker-{i}"))
            self.task_workers.append(worker)

        # Validate Pi connectivity
        if not await self._validate_pi_connection():
            raise ConnectionError(f"Failed to connect to Pi at {self.pi_ip}")

        logger.info("🚀 Gigabit Pi offload client initialized (Pi: %s)", self.pi_ip)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """🔚 Async context manager exit"""
        # Cancel all workers
        for worker in self.task_workers:
            worker.cancel()

        if hasattr(self, 'session'):
            await self.session.close()
        await self.connector.close()

        self.logger.info("🔚 Gigabit Pi offload client closed")

    async def _validate_pi_connection(self) -> bool:
        """🔍 Validate connection to Pi micro-cloud"""
        try:
            async with self.session.get(f"{self.pi_base_url}/health") as response:
                if response.status == 200:
                    data = await response.json()
        logger.info("✅ Pi connection validated: %s", data.get('status', 'unknown'))
                    return True
                else:
        logger.error("❌ Pi health check failed: HTTP %s", response.status)
                    return False
        except (socket.error, ConnectionError, requests.RequestException) as e:
        logger.error("❌ Pi connection validation failed: %s", e)
            return False

    def _monitor_performance(self):
        """📊 Background performance monitoring"""
        while True:
            try:
                # Monitor network utilization
                net_io = psutil.net_io_counters()
                self.metrics['network_utilization'] = (net_io.bytes_sent + net_io.bytes_recv) / 1_000_000  # MB

                # Update connection pool usage
                if hasattr(self, 'connector'):
                    self.metrics['connection_pool_usage'] = len(self.connector._conns)

                # Calculate average execution time
                if self.metrics['tasks_completed'] > 0:
                    total_execution_time = sum([
                        task.get('execution_time', 0)
                        for task in self.active_tasks.values()
                    ])
                    self.metrics['avg_execution_time'] = total_execution_time / self.metrics['tasks_completed']

                time.sleep(10)  # Update every 10 seconds
            except (socket.error, ConnectionError, requests.RequestException) as e:
        logger.warning("Performance monitoring error: %s", e)
                time.sleep(30)

    async def _task_worker(self, worker_id: str):
        """🔄 Background task worker for processing offload queue"""
        logger.info("🔄 Task worker %s started", worker_id)

        while True:
            try:
                # Get task from queue
                task = await self.task_queue.get()

                # Process task
                start_time = time.time()
                result = await self._execute_single_task(task)
                execution_time = time.time() - start_time

                # Update metrics
                self.metrics['tasks_completed'] += 1

                # Store result
                result.execution_time = execution_time
                await self.results_queue.put(result)

                # Mark task as done
                self.task_queue.task_done()

                # Remove from active tasks
                if task.task_id in self.active_tasks:
                    del self.active_tasks[task.task_id]

            except asyncio.CancelledError:
        logger.info("🔚 Task worker %s cancelled", worker_id)
                break
            except (socket.error, ConnectionError, requests.RequestException) as e:
        logger.error("❌ Task worker {worker_id} error: %s", e)
                self.metrics['tasks_failed'] += 1

    async def _execute_single_task(self, task: OffloadTask) -> TaskResult:
        """⚡ Execute a single task on Pi"""
        try:
            # Prepare task payload
            task_payload = {
                'task_type': task.task_type,
                'payload': task.payload,
                'priority': task.priority,
                'client_id': 'gigabit-laptop-client',
                'timestamp': datetime.now().isoformat()
            }

            # Send task to Pi
            async with self.session.post(
                f"{self.pi_base_url}/api/offload",
                json=task_payload,
                timeout=task.timeout
            ) as response:

                if response.status == 200:
                    result_data = await response.json()
                    return TaskResult(
                        task_id=task.task_id,
                        status="completed",
                        result=result_data,
                        pi_node_id=result_data.get('pi_node_id', 'unknown')
                    )
                else:
                    error_msg = f"HTTP {response.status}: {await response.text()}"
                    return TaskResult(
                        task_id=task.task_id,
                        status="failed",
                        error=error_msg
                    )

        except asyncio.TimeoutError:
            return TaskResult(
                task_id=task.task_id,
                status="timeout",
                error=f"Task timed out after {task.timeout}s"
            )
        except (socket.error, ConnectionError, requests.RequestException) as e:
            return TaskResult(
                task_id=task.task_id,
                status="error",
                error=str(e)
            )

    async def submit_task(self, task: OffloadTask) -> str:
        """📤 Submit a task for Pi offloading"""
        if not task.task_id:
            task.task_id = f"task_{uuid.uuid4().hex[:8]}"

        # Add to active tasks
        self.active_tasks[task.task_id] = {
            'task': task,
            'submitted_at': time.time(),
            'status': 'queued'
        }

        # Add to processing queue
        await self.task_queue.put(task)
        self.metrics['tasks_submitted'] += 1

        logger.info("📤 Task {task.task_id} submitted (%s)", task.task_type)
        return task.task_id

    async def submit_batch_tasks(self, tasks: List[OffloadTask]) -> List[str]:
        """📦 Submit multiple tasks as a batch"""
        task_ids = []

        for task in tasks:
            task_id = await self.submit_task(task)
            task_ids.append(task_id)

        logger.info("📦 Batch of %s tasks submitted", len(tasks))
        return task_ids

    async def wait_for_task(self, task_id: str, timeout: Optional[float] = None) -> TaskResult:
        """⏳ Wait for a specific task to complete"""
        start_time = time.time()

        while True:
            # Check if task is still active
            if task_id not in self.active_tasks:
                # Try to get result from queue
                try:
                    while True:
                        result = await asyncio.wait_for(self.results_queue.get(), timeout=1.0)
                        if result.task_id == task_id:
                            return result
                        else:
                            # Put back non-matching result
                            await self.results_queue.put(result)
                except asyncio.TimeoutError:
                    pass

            # Check timeout
            if timeout and (time.time() - start_time) > timeout:
                return TaskResult(
                    task_id=task_id,
                    status="timeout",
                    error=f"Wait timeout after {timeout}s"
                )

            await asyncio.sleep(0.1)

    async def wait_for_all_tasks(self, task_ids: List[str], timeout: Optional[float] = None) -> List[TaskResult]:
        """⏳ Wait for all specified tasks to complete"""
        results = []
        pending_tasks = set(task_ids)
        start_time = time.time()

        while pending_tasks:
            try:
                result = await asyncio.wait_for(self.results_queue.get(), timeout=1.0)
                if result.task_id in pending_tasks:
                    results.append(result)
                    pending_tasks.remove(result.task_id)
                else:
                    # Put back non-matching result
                    await self.results_queue.put(result)
            except asyncio.TimeoutError:
                pass

            # Check timeout
            if timeout and (time.time() - start_time) > timeout:
                # Return partial results with timeout status for remaining
                for task_id in pending_tasks:
                    results.append(TaskResult(
                        task_id=task_id,
                        status="timeout",
                        error=f"Wait timeout after {timeout}s"
                    ))
                break

            await asyncio.sleep(0.1)

        return results

    def get_metrics(self) -> Dict[str, Any]:
        """📊 Get current performance metrics"""
        return {
            **self.metrics,
            'active_tasks': len(self.active_tasks),
            'queue_size': self.task_queue.qsize(),
            'results_pending': self.results_queue.qsize(),
            'workers_active': len([w for w in self.task_workers if not w.done()]),
            'pi_ip': self.pi_ip
        }

    async def get_pi_status(self) -> Dict[str, Any]:
        """📊 Get Pi micro-cloud status"""
        try:
            async with self.session.get(f"{self.pi_base_url}/pi/status") as response:
                if response.status == 200:
                    return await response.json()
                else:
                    return {'error': f'HTTP {response.status}'}
        except (socket.error, ConnectionError, requests.RequestException) as e:
            return {'error': str(e)}

# 🎯 Example Usage Functions

async def example_compute_offloading():
    """🧮 Example: Offload computational tasks to Pi"""
    async with GigabitPiOffloadClient() as client:
        # Create computational tasks
        tasks = []
        for i in range(10):
            task = OffloadTask(
                task_id=f"compute_{i}",
                task_type="heavy_computation",
                payload={
                    'operation': 'matrix_multiply',
                    'matrix_size': 100,
                    'iterations': 1000
                },
                priority="high" if i < 3 else "normal"
            )
            tasks.append(task)

        # Submit batch
        print("📤 Submitting computational tasks...")
        task_ids = await client.submit_batch_tasks(tasks)

        # Wait for completion
        print("⏳ Waiting for tasks to complete...")
        results = await client.wait_for_all_tasks(task_ids, timeout=120)

        # Print results
        successful = [r for r in results if r.status == "completed"]
        print(f"✅ {len(successful)}/{len(results)} tasks completed successfully")

        # Show metrics
        metrics = client.get_metrics()
        print(f"📊 Avg execution time: {metrics['avg_execution_time']:.2f}s")

async def example_data_processing_offloading():
    """📊 Example: Offload data processing tasks to Pi"""
    async with GigabitPiOffloadClient() as client:
        # Create data processing task
        task = OffloadTask(
            task_id="data_processing_001",
            task_type="data_analysis",
            payload={
                'operation': 'statistical_analysis',
                'dataset_size': 10000,
                'analysis_type': 'correlation_matrix'
            },
            timeout=60
        )

        print("📊 Submitting data processing task...")
        task_id = await client.submit_task(task)

        # Monitor progress
        result = await client.wait_for_task(task_id, timeout=120)

        if result.status == "completed":
            print(f"✅ Data processing completed: {result.result}")
        else:
            print(f"❌ Task failed: {result.error}")

async def performance_benchmark():
    """⚡ Performance benchmark for Gigabit connection"""
    async with GigabitPiOffloadClient(max_concurrent_tasks=25) as client:
        print("🚀 Starting Gigabit performance benchmark...")

        # Create high-load test
        tasks = []
        for i in range(50):
            task = OffloadTask(
                task_id=f"benchmark_{i}",
                task_type="performance_test",
                payload={
                    'test_type': 'throughput',
                    'data_size': 1024 * 100,  # 100KB
                    'compute_cycles': 1000
                }
            )
            tasks.append(task)

        start_time = time.time()

        # Submit all tasks
        task_ids = await client.submit_batch_tasks(tasks)

        # Wait for completion
        results = await client.wait_for_all_tasks(task_ids, timeout=180)

        end_time = time.time()
        total_duration = end_time - start_time

        # Calculate performance metrics
        successful = [r for r in results if r.status == "completed"]
        success_rate = len(successful) / len(results)
        avg_execution_time = sum(r.execution_time for r in successful) / len(successful) if successful else 0
        tasks_per_second = len(successful) / total_duration

        print(f"\n📊 GIGABIT PERFORMANCE BENCHMARK RESULTS")
        print("=" * 50)
        print(f"Total Tasks: {len(tasks)}")
        print(f"Successful: {len(successful)} ({success_rate*100:.1f}%)")
        print(f"Total Duration: {total_duration:.2f}s")
        print(f"Tasks/Second: {tasks_per_second:.2f}")
        print(f"Avg Execution Time: {avg_execution_time:.3f}s")

        # Get final metrics
        metrics = client.get_metrics()
        print(f"Network Utilization: {metrics['network_utilization']:.2f} MB")
        print(f"Active Connections: {metrics['connection_pool_usage']}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Gigabit Pi Offload Client")
    parser.add_argument('--pi-ip', default='192.168.1.200', help='Pi IP address')
    parser.add_argument('--example', choices=['compute', 'data', 'benchmark'],
                       default='benchmark', help='Example to run')

    args = parser.parse_args()

    # Override client IP
    GigabitPiOffloadClient.__init__ = lambda self, pi_ip=args.pi_ip, **kwargs: \
        GigabitPiOffloadClient.__init__(self, pi_ip=pi_ip, **kwargs)

    if args.example == 'compute':
        asyncio.run(example_compute_offloading())
    elif args.example == 'data':
        asyncio.run(example_data_processing_offloading())
    elif args.example == 'benchmark':
        asyncio.run(performance_benchmark())
