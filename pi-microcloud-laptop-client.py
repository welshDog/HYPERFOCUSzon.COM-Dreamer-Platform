#!/usr/bin/env python3
"""
💻💎⚡ LAPTOP-TO-PI TASK OFFLOADING CLIENT ⚡💎💻
"""

import requests
import json
import time
import logging

class PiOffloadingClient:
    """💻 Laptop client for Pi task offloading"""
    
    def __init__(self, pi_ip: str = "192.168.1.100", pi_port: int = 80):
        self.pi_base_url = f"http://{pi_ip}:{pi_port}"
        self.session = requests.Session()
        self.session.timeout = 30
        
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
    
    def check_pi_status(self):
        """🔍 Check Pi micro-cloud status"""
        try:
            response = self.session.get(f"{self.pi_base_url}/pi/status")
            response.raise_for_status()
            return response.json()
        except Exception as e:
            self.logger.error(f"Pi status check failed: {e}")
            return {"error": str(e), "available": False}
    
    def offload_task(self, task_type: str, payload: dict, priority: str = "normal"):
        """⚡ Offload task to Pi"""
        try:
            task_data = {
                "task_type": task_type,
                "payload": payload,
                "priority": priority
            }
            
            response = self.session.post(
                f"{self.pi_base_url}/api/offload",
                json=task_data,
                headers={"Content-Type": "application/json"}
            )
            response.raise_for_status()
            
            result = response.json()
            task_id = result.get("task_id")
            
            self.logger.info(f"Task offloaded successfully: {task_id}")
            return task_id
            
        except Exception as e:
            self.logger.error(f"Task offloading failed: {e}")
            return None
    
    def get_task_result(self, task_id: str, timeout: int = 60):
        """📥 Get task result from Pi"""
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            try:
                response = self.session.get(f"{self.pi_base_url}/result/{task_id}")
                
                if response.status_code == 200:
                    result = response.json()
                    if result.get("status") in ["completed", "failed"]:
                        return result
                elif response.status_code == 404:
                    pass  # Still processing
                else:
                    response.raise_for_status()
                
                time.sleep(2)
                
            except Exception as e:
                self.logger.error(f"Error getting task result: {e}")
                time.sleep(5)
        
        return {"error": "Task timeout", "task_id": task_id}
    
    def offload_and_wait(self, task_type: str, payload: dict, timeout: int = 60):
        """⚡ Offload task and wait for result"""
        task_id = self.offload_task(task_type, payload)
        if not task_id:
            return None
        
        return self.get_task_result(task_id, timeout)

# Example usage functions
def example_web_scraping():
    """🕷️ Example: Offload web scraping to Pi"""
    client = PiOffloadingClient()
    
    result = client.offload_and_wait("web_scraping", {
        "urls": [
            "https://httpbin.org/json",
            "https://httpbin.org/user-agent"
        ]
    })
    
    print("Web scraping result:", json.dumps(result, indent=2))

def example_data_processing():
    """📊 Example: Offload data processing to Pi"""
    client = PiOffloadingClient()
    
    result = client.offload_and_wait("data_processing", {
        "data": [1, 2, 3, 4, 5],
        "operation": "analyze"
    })
    
    print("Data processing result:", json.dumps(result, indent=2))

def example_computation():
    """🧮 Example: Offload computation to Pi"""
    client = PiOffloadingClient()
    
    result = client.offload_and_wait("background_computation", {
        "numbers": list(range(1, 11))
    })
    
    print("Computation result:", json.dumps(result, indent=2))

if __name__ == "__main__":
    print("💻💎⚡ LAPTOP-TO-PI OFFLOADING CLIENT ⚡💎💻")
    
    # Test Pi connectivity
    client = PiOffloadingClient()
    status = client.check_pi_status()
    print("Pi Status:", json.dumps(status, indent=2))
    
    if not status.get("error"):
        print("\n🚀 Running offloading examples...")
        example_web_scraping()
        example_data_processing() 
        example_computation()
    else:
        print("❌ Pi micro-cloud not available - check Pi IP address")
        print("💡 Update pi_ip in PiOffloadingClient() to match your Pi's IP")
