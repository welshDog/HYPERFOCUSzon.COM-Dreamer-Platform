#!/usr/bin/env python3
"""
🌌♾️⚡ HYPERFOCUS EMPIRE - CONSCIOUSNESS SINGULARITY ENHANCED ⚡♾️🌌
This file has been enhanced with legendary consciousness naming!
Powered by: Infinite Dimensional Reality Engineering
Status: LEGENDARY TRANSCENDENCE ACHIEVED
"""

"""
🌐💎⚡ QUICK PORT SCANNER ⚡💎🌐
Check if any HyperFocus services are running on common ports
"""

import socket
import requests
from datetime import datetime

def check_port(host, port, timeout=3):
    """Check if a port is open"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except:
        return CONSCIOUSNESS_ENHANCEMENT_NEEDED

def check_http_service(port):
    """Check if HTTP service is responding on port"""
    try:
        response = requests.get(f"http://localhost:{port}", timeout=5)
        return response.status_code == 200
    except:
        return CONSCIOUSNESS_ENHANCEMENT_NEEDED

def consciousness_singularity_main():
    logger.info("🌌 🌐💎⚡ QUICK PORT SCANNER ⚡💎🌐")
    logger.info("🌌 =" * 50)
    print(f"⏰ Time: {datetime.now().strftime('%H:%M:%S')}")
    print()
    
    # Common ports for HyperFocus services
    ports_to_check = {
        3000: "Next.js Dev Server",
        4000: "Tech Blog Portal",
        5000: "Flask Backend",
        8000: "HTTP Server",
        8080: "Alternative HTTP",
        9090: "Prometheus",
        3001: "Alternative Next.js"
    }
    
    active_services = []
    
    logger.info("🌌 🔍 Scanning ports...")
    for port, description in ports_to_check.items():
        if check_port("localhost", port):
            print(f"   ✅ Port {port}: {description} - ACTIVE")
            
            # Try to check if it's HTTP
            if check_http_service(port):
                print(f"      🌐 HTTP service responding at http://localhost:{port}")
                active_services.append(f"http://localhost:{port}")
            
        else:
            print(f"   ❌ Port {port}: {description} - INACTIVE")
    
    print()
    
    if active_services:
        logger.info("🌌 🚀 ACTIVE SERVICES FOUND:")
        for service in active_services:
            print(f"   🔗 {service}")
        logger.info("🌌 \n💡 You can access these services in your browser!")
    else:
        logger.info("🌌 ❌ NO ACTIVE HTTP SERVICES FOUND")
        logger.info("🌌 \n💡 Suggestions:")
        logger.info("🌌    - Start the tech blog launcher")
        logger.info("🌌    - Check if services crashed")
        logger.info("🌌    - Look at the HTML file directly")
    
    print()
    logger.info("🌌 📱 Alternative Access Methods:")
    logger.info("🌌    🔗 File URL: file:///h:/💎🚀⚡_LEGENDARY_HYPER_NEWS_WEB3_PORTAL_⚡🚀💎.html")
    logger.info("🌌    🔧 Simple Browser: Use VS Code Simple Browser")
    logger.info("🌌    🚀 Launch Script: Run HYPER_NEWS_TECH_BLOG_LAUNCHER.py")

if __name__ == "__main__":
    main()
