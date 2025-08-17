#!/usr/bin/env python3
from datetime import datetime
import json

import requests
class PiClientTester:
    def __init__(self):
        self.pi_ip = "192.168.137.100"

    def test_connectivity(self):
        try:
            response = requests.get(f"http://{self.pi_ip}/health", timeout=5)
            return response.status_code == 200
        except (ConnectionError, OSError):
            return False

    def test_broskie_agent(self):
        try:
            response = requests.post(
                f"http://{self.pi_ip}:8080/process",
                json={"task_id": "test", "data": "validation"},
                timeout=10
            )
            return response.status_code == 200
        except (ConnectionError, OSError):
            return False

    def run_tests(self):
        print("🧪 LEGENDARY Pi Client Testing Suite")
        print("=" * 40)

        connectivity = self.test_connectivity()
        print(f"🔍 Connectivity: {'✅ PASS' if connectivity else '❌ FAIL'}")

        if connectivity:
            agent_test = self.test_broskie_agent()
            print(f"🤖 BROski Agent: {'✅ PASS' if agent_test else '❌ FAIL'}")

            if agent_test:
                print("\n🏆 Pi micro-cloud is LEGENDARY-ready!")
            else:
                print("\n⚠️ Agent needs attention")
        else:
            print("\n❌ Pi not reachable - check connection")

if __name__ == "__main__":
    tester = PiClientTester()
    tester.run_tests()
