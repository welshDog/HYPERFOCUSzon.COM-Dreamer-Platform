#!/bin/bash
# Test HyperFocus Zone AI Assistant

echo "Testing HyperFocus Zone AI Assistant..."
echo "========================================"

echo "1. Health check:"
curl -s http://localhost:8888/health | jq '.' 2>/dev/null || curl -s http://localhost:8888/health

echo -e "\n2. Welcome page:"
curl -s http://localhost:8888/ | jq '.message' 2>/dev/null || curl -s http://localhost:8888/

echo -e "\n3. Techniques list:"
curl -s http://localhost:8888/techniques | jq '.techniques | keys' 2>/dev/null || curl -s http://localhost:8888/techniques

echo -e "\n4. Specific technique (Modified Pomodoro):"
curl -s http://localhost:8888/techniques/1 | jq '.technique.name' 2>/dev/null || curl -s http://localhost:8888/techniques/1

echo -e "\n5. Chat test (ADHD help):"
curl -s -X POST http://localhost:8888/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "I have ADHD and need help focusing"}' | jq '.response' 2>/dev/null || \
curl -s -X POST http://localhost:8888/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "I have ADHD and need help focusing"}'

echo -e "\n6. Chat test (Autism support):"
curl -s -X POST http://localhost:8888/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "I am autistic and feeling overwhelmed"}' | jq '.response' 2>/dev/null || \
curl -s -X POST http://localhost:8888/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "I am autistic and feeling overwhelmed"}'

echo -e "\n=================================="
echo "AI Assistant test complete!"
echo "If all tests passed, your empire is ready to help neurodivergent individuals! 🚀"
