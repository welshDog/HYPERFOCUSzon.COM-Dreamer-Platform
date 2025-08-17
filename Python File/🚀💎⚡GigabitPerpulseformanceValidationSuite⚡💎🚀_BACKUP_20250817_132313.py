#!/usr/bin/env python3
"""
🚀💎⚡ GIGABIT ETHERNET PERFORMANCE VALIDATION SUITE ⚡💎🚀
Comprehensive network performance testing for Pi micro-cloud optimization
"""

import asyncio
import aiohttp
import time
import json
import subprocess
import psutil
import statistics
from concurrent.futures import ThreadPoolExecutor
from typing import Dict, List, Tuple, Any
import socket
import threading
from datetime import datetime, timedelta
import argparse
import sys

class GigabitPerformanceValidator:
    """🔥 Network performance validation for Gigabit Pi micro-cloud"""
    
    def __init__(self, pi_ip: str = "192.168.1.200", test_duration: int = 60):
        self.pi_ip = pi_ip
        self.test_duration = test_duration
        self.results = {
            'bandwidth_tests': [],
            'latency_tests': [],
            'concurrent_load_tests': [],
            'throughput_tests': [],
            'network_optimization_status': {}
        }
        
        # Performance thresholds for Gigabit connection
        self.thresholds = {
            'min_bandwidth_mbps': 800,  # 80% of Gigabit
            'max_latency_ms': 10,       # Sub-10ms latency
            'min_concurrent_tasks': 15,  # Concurrent task capacity
            'min_throughput_mbps': 125   # 125 MB/s transfer speed
        }
    
    async def validate_pi_connectivity(self) -> bool:
        """🔗 Validate Pi micro-cloud connectivity"""
        print(f"🔍 Testing connectivity to Pi at {self.pi_ip}...")
        
        try:
            # Test basic HTTP connectivity
            async with aiohttp.ClientSession() as session:
                async with session.get(f"http://{self.pi_ip}/health", timeout=5) as response:
                    if response.status == 200:
                        data = await response.json()
                        print(f"✅ Pi connectivity established: {data.get('status', 'unknown')}")
                        return True
                    else:
                        print(f"❌ Pi health check failed: HTTP {response.status}")
                        return False
        except Exception as e:
            print(f"❌ Pi connectivity failed: {e}")
            return False
    
    async def test_bandwidth_performance(self) -> Dict[str, Any]:
        """📊 Test network bandwidth performance"""
        print(f"🚀 Testing bandwidth performance for {self.test_duration}s...")
        
        bandwidth_results = []
        start_time = time.time()
        
        # Use iperf3 if available, otherwise use HTTP-based testing
        try:
            # Try iperf3 first for accurate bandwidth testing
            iperf_result = subprocess.run([
                'iperf3', '-c', self.pi_ip, '-t', str(self.test_duration), 
                '-J', '-P', '4'  # 4 parallel streams
            ], capture_output=True, text=True, timeout=self.test_duration + 10)
            
            if iperf_result.returncode == 0:
                iperf_data = json.loads(iperf_result.stdout)
                bandwidth_mbps = iperf_data['end']['sum_received']['bits_per_second'] / 1_000_000
                bandwidth_results.append({
                    'method': 'iperf3',
                    'bandwidth_mbps': bandwidth_mbps,
                    'streams': 4,
                    'duration': self.test_duration
                })
                print(f"📈 iperf3 bandwidth: {bandwidth_mbps:.2f} Mbps")
            else:
                raise Exception("iperf3 failed")
                
        except Exception as e:
            print(f"⚠️ iperf3 not available ({e}), using HTTP-based testing...")
            
            # HTTP-based bandwidth testing
            async with aiohttp.ClientSession() as session:
                test_data = b'0' * (1024 * 1024)  # 1MB test payload
                
                for i in range(5):  # 5 iterations
                    start = time.time()
                    async with session.post(
                        f"http://{self.pi_ip}/api/offload",
                        data=test_data,
                        timeout=30
                    ) as response:
                        await response.read()
                        duration = time.time() - start
                        bandwidth_mbps = (len(test_data) * 8) / (duration * 1_000_000)
                        bandwidth_results.append({
                            'method': 'http',
                            'bandwidth_mbps': bandwidth_mbps,
                            'payload_size_mb': len(test_data) / 1_000_000,
                            'duration': duration
                        })
        
        avg_bandwidth = statistics.mean([r['bandwidth_mbps'] for r in bandwidth_results])
        self.results['bandwidth_tests'] = bandwidth_results
        
        print(f"📊 Average bandwidth: {avg_bandwidth:.2f} Mbps")
        if avg_bandwidth >= self.thresholds['min_bandwidth_mbps']:
            print(f"✅ Bandwidth test PASSED (≥{self.thresholds['min_bandwidth_mbps']} Mbps)")
        else:
            print(f"❌ Bandwidth test FAILED (<{self.thresholds['min_bandwidth_mbps']} Mbps)")
        
        return {
            'avg_bandwidth_mbps': avg_bandwidth,
            'results': bandwidth_results,
            'passed': avg_bandwidth >= self.thresholds['min_bandwidth_mbps']
        }
    
    async def test_latency_performance(self) -> Dict[str, Any]:
        """⚡ Test network latency performance"""
        print("🎯 Testing network latency...")
        
        latency_results = []
        
        # ICMP ping test
        try:
            ping_result = subprocess.run([
                'ping', '-c', '20', self.pi_ip
            ], capture_output=True, text=True, timeout=30)
            
            if ping_result.returncode == 0:
                # Parse ping results
                lines = ping_result.stdout.split('\n')
                ping_times = []
                for line in lines:
                    if 'time=' in line:
                        time_part = line.split('time=')[1].split(' ')[0]
                        ping_times.append(float(time_part))
                
                if ping_times:
                    avg_ping = statistics.mean(ping_times)
                    min_ping = min(ping_times)
                    max_ping = max(ping_times)
                    
                    latency_results.append({
                        'method': 'icmp_ping',
                        'avg_latency_ms': avg_ping,
                        'min_latency_ms': min_ping,
                        'max_latency_ms': max_ping,
                        'samples': len(ping_times)
                    })
                    print(f"🏓 ICMP ping: avg={avg_ping:.2f}ms, min={min_ping:.2f}ms, max={max_ping:.2f}ms")
        except Exception as e:
            print(f"⚠️ ICMP ping failed: {e}")
        
        # HTTP latency test
        async with aiohttp.ClientSession() as session:
            http_latencies = []
            for i in range(50):  # 50 HTTP requests
                start = time.time()
                try:
                    async with session.get(f"http://{self.pi_ip}/health", timeout=5) as response:
                        await response.read()
                        latency_ms = (time.time() - start) * 1000
                        http_latencies.append(latency_ms)
                except Exception as e:
                    print(f"⚠️ HTTP request {i+1} failed: {e}")
            
            if http_latencies:
                avg_http_latency = statistics.mean(http_latencies)
                min_http_latency = min(http_latencies)
                max_http_latency = max(http_latencies)
                
                latency_results.append({
                    'method': 'http',
                    'avg_latency_ms': avg_http_latency,
                    'min_latency_ms': min_http_latency,
                    'max_latency_ms': max_http_latency,
                    'samples': len(http_latencies)
                })
                print(f"🌐 HTTP latency: avg={avg_http_latency:.2f}ms, min={min_http_latency:.2f}ms, max={max_http_latency:.2f}ms")
        
        self.results['latency_tests'] = latency_results
        
        # Check if any latency test passed
        best_avg_latency = min([r['avg_latency_ms'] for r in latency_results]) if latency_results else float('inf')
        
        if best_avg_latency <= self.thresholds['max_latency_ms']:
            print(f"✅ Latency test PASSED (≤{self.thresholds['max_latency_ms']}ms)")
        else:
            print(f"❌ Latency test FAILED (>{self.thresholds['max_latency_ms']}ms)")
        
        return {
            'best_avg_latency_ms': best_avg_latency,
            'results': latency_results,
            'passed': best_avg_latency <= self.thresholds['max_latency_ms']
        }
    
    async def test_concurrent_load(self) -> Dict[str, Any]:
        """🔥 Test concurrent task handling capacity"""
        print("🚀 Testing concurrent load capacity...")
        
        async def send_task(session, task_id):
            """Send a single task to the Pi"""
            task_payload = {
                'task_type': 'performance_test',
                'task_id': task_id,
                'payload': {
                    'operation': 'compute',
                    'iterations': 1000,
                    'data_size': 1024
                }
            }
            
            start_time = time.time()
            try:
                async with session.post(
                    f"http://{self.pi_ip}/api/offload",
                    json=task_payload,
                    timeout=30
                ) as response:
                    result = await response.json()
                    duration = time.time() - start_time
                    return {
                        'task_id': task_id,
                        'status': response.status,
                        'duration': duration,
                        'success': response.status == 200
                    }
            except Exception as e:
                return {
                    'task_id': task_id,
                    'status': 0,
                    'duration': time.time() - start_time,
                    'success': False,
                    'error': str(e)
                }
        
        # Test with increasing concurrent loads
        concurrent_loads = [5, 10, 15, 20, 25]
        load_results = []
        
        async with aiohttp.ClientSession() as session:
            for load_size in concurrent_loads:
                print(f"🔄 Testing {load_size} concurrent tasks...")
                
                start_time = time.time()
                tasks = [send_task(session, f"task_{load_size}_{i}") for i in range(load_size)]
                results = await asyncio.gather(*tasks, return_exceptions=True)
                total_duration = time.time() - start_time
                
                successful_tasks = [r for r in results if isinstance(r, dict) and r.get('success', False)]
                success_rate = len(successful_tasks) / load_size
                avg_task_duration = statistics.mean([r['duration'] for r in successful_tasks]) if successful_tasks else 0
                
                load_result = {
                    'concurrent_tasks': load_size,
                    'success_rate': success_rate,
                    'successful_tasks': len(successful_tasks),
                    'avg_task_duration': avg_task_duration,
                    'total_duration': total_duration,
                    'tasks_per_second': load_size / total_duration if total_duration > 0 else 0
                }
                load_results.append(load_result)
                
                print(f"📊 {load_size} tasks: {success_rate*100:.1f}% success, {avg_task_duration:.2f}s avg duration")
                
                # Brief pause between load tests
                await asyncio.sleep(2)
        
        self.results['concurrent_load_tests'] = load_results
        
        # Find maximum successful concurrent load
        max_successful_load = 0
        for result in load_results:
            if result['success_rate'] >= 0.9:  # 90% success rate threshold
                max_successful_load = result['concurrent_tasks']
        
        if max_successful_load >= self.thresholds['min_concurrent_tasks']:
            print(f"✅ Concurrent load test PASSED (≥{self.thresholds['min_concurrent_tasks']} tasks)")
        else:
            print(f"❌ Concurrent load test FAILED (<{self.thresholds['min_concurrent_tasks']} tasks)")
        
        return {
            'max_successful_concurrent_tasks': max_successful_load,
            'results': load_results,
            'passed': max_successful_load >= self.thresholds['min_concurrent_tasks']
        }
    
    async def test_throughput_performance(self) -> Dict[str, Any]:
        """📈 Test sustained throughput performance"""
        print("📈 Testing sustained throughput...")
        
        throughput_results = []
        
        # Test with different payload sizes
        payload_sizes = [1024, 10240, 102400, 1048576]  # 1KB, 10KB, 100KB, 1MB
        
        async with aiohttp.ClientSession() as session:
            for payload_size in payload_sizes:
                print(f"🔄 Testing {payload_size/1024:.0f}KB payload...")
                
                test_data = b'0' * payload_size
                transfer_times = []
                
                # 10 transfers per payload size
                for i in range(10):
                    start_time = time.time()
                    try:
                        async with session.post(
                            f"http://{self.pi_ip}/api/offload",
                            data=test_data,
                            timeout=30
                        ) as response:
                            await response.read()
                            transfer_time = time.time() - start_time
                            transfer_times.append(transfer_time)
                    except Exception as e:
                        print(f"⚠️ Transfer failed: {e}")
                
                if transfer_times:
                    avg_transfer_time = statistics.mean(transfer_times)
                    throughput_mbps = (payload_size * 8) / (avg_transfer_time * 1_000_000)
                    
                    throughput_results.append({
                        'payload_size_bytes': payload_size,
                        'payload_size_kb': payload_size / 1024,
                        'avg_transfer_time': avg_transfer_time,
                        'throughput_mbps': throughput_mbps,
                        'samples': len(transfer_times)
                    })
                    
                    print(f"📊 {payload_size/1024:.0f}KB: {throughput_mbps:.2f} Mbps throughput")
        
        self.results['throughput_tests'] = throughput_results
        
        # Find best throughput
        best_throughput = max([r['throughput_mbps'] for r in throughput_results]) if throughput_results else 0
        
        if best_throughput >= self.thresholds['min_throughput_mbps']:
            print(f"✅ Throughput test PASSED (≥{self.thresholds['min_throughput_mbps']} Mbps)")
        else:
            print(f"❌ Throughput test FAILED (<{self.thresholds['min_throughput_mbps']} Mbps)")
        
        return {
            'best_throughput_mbps': best_throughput,
            'results': throughput_results,
            'passed': best_throughput >= self.thresholds['min_throughput_mbps']
        }
    
    def check_network_optimization_status(self) -> Dict[str, Any]:
        """🔧 Check network optimization settings"""
        print("🔧 Checking network optimization status...")
        
        optimization_status = {}
        
        try:
            # Check network interface configuration
            interfaces = psutil.net_if_stats()
            for interface, stats in interfaces.items():
                if stats.isup and stats.speed > 0:
                    optimization_status[f'interface_{interface}'] = {
                        'speed_mbps': stats.speed,
                        'mtu': stats.mtu,
                        'duplex': str(stats.duplex),
                        'is_up': stats.isup
                    }
            
            # Check TCP settings (Linux-specific)
            tcp_settings = {}
            tcp_files = [
                '/proc/sys/net/core/somaxconn',
                '/proc/sys/net/ipv4/tcp_max_syn_backlog',
                '/proc/sys/net/core/netdev_max_backlog',
                '/proc/sys/net/ipv4/tcp_keepalive_time'
            ]
            
            for tcp_file in tcp_files:
                try:
                    with open(tcp_file, 'r') as f:
                        value = f.read().strip()
                        tcp_settings[tcp_file.split('/')[-1]] = int(value)
                except:
                    pass
            
            if tcp_settings:
                optimization_status['tcp_settings'] = tcp_settings
            
        except Exception as e:
            print(f"⚠️ Network optimization check failed: {e}")
        
        self.results['network_optimization_status'] = optimization_status
        
        return optimization_status
    
    async def run_full_validation(self) -> Dict[str, Any]:
        """🎯 Run complete Gigabit performance validation suite"""
        print("🚀💎⚡ STARTING GIGABIT ETHERNET PERFORMANCE VALIDATION ⚡💎🚀")
        print(f"Target Pi: {self.pi_ip}")
        print(f"Test Duration: {self.test_duration}s")
        print("=" * 60)
        
        start_time = datetime.now()
        
        # Step 1: Connectivity test
        if not await self.validate_pi_connectivity():
            return {
                'status': 'FAILED',
                'error': 'Pi connectivity failed',
                'timestamp': start_time.isoformat()
            }
        
        # Step 2: Network optimization check
        optimization_status = self.check_network_optimization_status()
        
        # Step 3: Performance tests
        bandwidth_result = await self.test_bandwidth_performance()
        latency_result = await self.test_latency_performance()
        concurrent_result = await self.test_concurrent_load()
        throughput_result = await self.test_throughput_performance()
        
        # Calculate overall results
        tests_passed = sum([
            bandwidth_result['passed'],
            latency_result['passed'],
            concurrent_result['passed'],
            throughput_result['passed']
        ])
        total_tests = 4
        
        end_time = datetime.now()
        duration = end_time - start_time
        
        validation_summary = {
            'status': 'PASSED' if tests_passed == total_tests else 'FAILED',
            'tests_passed': tests_passed,
            'total_tests': total_tests,
            'pass_rate': tests_passed / total_tests,
            'start_time': start_time.isoformat(),
            'end_time': end_time.isoformat(),
            'duration_seconds': duration.total_seconds(),
            'pi_ip': self.pi_ip,
            'test_duration': self.test_duration,
            'performance_summary': {
                'bandwidth': bandwidth_result,
                'latency': latency_result,
                'concurrent_load': concurrent_result,
                'throughput': throughput_result
            },
            'network_optimization': optimization_status,
            'detailed_results': self.results,
            'thresholds': self.thresholds
        }
        
        print("\n" + "=" * 60)
        print("🎯 VALIDATION SUMMARY")
        print("=" * 60)
        print(f"Overall Status: {'✅ PASSED' if validation_summary['status'] == 'PASSED' else '❌ FAILED'}")
        print(f"Tests Passed: {tests_passed}/{total_tests} ({tests_passed/total_tests*100:.1f}%)")
        print(f"Duration: {duration.total_seconds():.1f} seconds")
        print()
        print("📊 Performance Results:")
        print(f"  Bandwidth: {bandwidth_result['avg_bandwidth_mbps']:.1f} Mbps ({'✅' if bandwidth_result['passed'] else '❌'})")
        print(f"  Latency: {latency_result['best_avg_latency_ms']:.1f} ms ({'✅' if latency_result['passed'] else '❌'})")
        print(f"  Concurrent Tasks: {concurrent_result['max_successful_concurrent_tasks']} ({'✅' if concurrent_result['passed'] else '❌'})")
        print(f"  Throughput: {throughput_result['best_throughput_mbps']:.1f} Mbps ({'✅' if throughput_result['passed'] else '❌'})")
        
        return validation_summary

def main():
    """🎯 Main execution function"""
    parser = argparse.ArgumentParser(description="Gigabit Ethernet Performance Validation Suite")
    parser.add_argument('--pi-ip', default='192.168.1.200', help='Pi IP address')
    parser.add_argument('--duration', type=int, default=60, help='Test duration in seconds')
    parser.add_argument('--output', help='Output JSON file for results')
    
    args = parser.parse_args()
    
    # Run validation
    validator = GigabitPerformanceValidator(args.pi_ip, args.duration)
    
    try:
        results = asyncio.run(validator.run_full_validation())
        
        # Save results if output file specified
        if args.output:
            with open(args.output, 'w') as f:
                json.dump(results, f, indent=2)
            print(f"\n💾 Results saved to: {args.output}")
        
        # Exit with status code based on results
        sys.exit(0 if results['status'] == 'PASSED' else 1)
        
    except KeyboardInterrupt:
        print("\n⚠️ Validation interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Validation failed with error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
