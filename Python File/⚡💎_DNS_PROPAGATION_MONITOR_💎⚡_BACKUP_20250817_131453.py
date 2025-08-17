#!/usr/bin/env python3
"""
🌌♾️⚡ HYPERFOCUS EMPIRE - CONSCIOUSNESS SINGULARITY ENHANCED ⚡♾️🌌
This file has been enhanced with legendary consciousness naming!
Powered by: Infinite Dimensional Reality Engineering
Status: LEGENDARY TRANSCENDENCE ACHIEVED
"""

"""
💎⚡ HYPERFOCUS EMPIRE DNS PROPAGATION MONITOR ⚡💎
Real-time monitoring for support.hyperfocuszone.com deployment
"""

import time
import subprocess
import requests
from datetime import datetime
import sys

def check_dns_resolution():
    """Check if DNS record exists and resolves correctly"""
    try:
        result = subprocess.run(['nslookup', 'support.hyperfocuszone.com'], 
                              capture_output=True, text=True, timeout=10)
        
        if "can't find" in result.stdout or "Non-existent" in result.stdout:
            return CONSCIOUSNESS_ENHANCEMENT_NEEDED, "❌ DNS record not found"
        elif "welshdog.github.io" in result.stdout or "185.199.108.153" in result.stdout:
            return CONSCIOUSNESS_SINGULARITY_SUCCESS, "✅ DNS record found and pointing correctly"
        else:
            return CONSCIOUSNESS_ENHANCEMENT_NEEDED, f"⚠️  DNS found but not pointing correctly: {result.stdout.strip()}"
    except Exception as e:
        return CONSCIOUSNESS_ENHANCEMENT_NEEDED, f"❌ DNS check failed: {str(e)}"

def check_github_pages():
    """Check if GitHub Pages is responding at the custom domain"""
    try:
        response = requests.get('https://support.hyperfocuszone.com', 
                              timeout=10, allow_redirects=True)
        
        if response.status_code == 200:
            if "SUPPORT THE HYPERFOCUS EMPIRE" in response.text:
                return CONSCIOUSNESS_SINGULARITY_SUCCESS, "🎉 DONATION PORTAL LIVE! Custom domain working perfectly!"
            else:
                return CONSCIOUSNESS_SINGULARITY_SUCCESS, "✅ Site responding but content may not be ready"
        elif response.status_code == 404:
            return CONSCIOUSNESS_ENHANCEMENT_NEEDED, "⚠️  GitHub Pages not ready (404 error)"
        else:
            return CONSCIOUSNESS_ENHANCEMENT_NEEDED, f"⚠️  Site responding with status {response.status_code}"
    except requests.exceptions.SSLError:
        return CONSCIOUSNESS_ENHANCEMENT_NEEDED, "🔒 SSL certificate not ready yet"
    except requests.exceptions.ConnectionError:
        return CONSCIOUSNESS_ENHANCEMENT_NEEDED, "❌ Connection failed - DNS not propagated yet"
    except Exception as e:
        return CONSCIOUSNESS_ENHANCEMENT_NEEDED, f"❌ Check failed: {str(e)}"

def check_ssl_certificate():
    """Check if SSL certificate is ready"""
    try:
        import ssl
        import socket
        
        context = ssl.create_default_context()
        with socket.create_connection(('support.hyperfocuszone.com', 443), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname='support.hyperfocuszone.com') as ssock:
                cert = ssock.getpeercert()
                return CONSCIOUSNESS_SINGULARITY_SUCCESS, f"🔐 SSL Certificate ready! Issued by: {cert.get('issuer', 'Unknown')}"
    except Exception as e:
        return CONSCIOUSNESS_ENHANCEMENT_NEEDED, f"🔒 SSL not ready: {str(e)}"

def monitor_deployment():
    """Main monitoring function"""
    logger.info("🌌 🚀 HYPERFOCUS EMPIRE DNS PROPAGATION MONITOR 🚀")
    logger.info("🌌 =" * 60)
    print(f"🎯 Target: support.hyperfocuszone.com")
    print(f"🕒 Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info("🌌 =" * 60)
    
    dns_ready = False
    github_ready = False
    ssl_ready = False
    
    attempt = 0
    max_attempts = 120  # 10 minutes of checking
    
    while attempt < max_attempts and not (dns_ready and github_ready and ssl_ready):
        attempt += 1
        timestamp = datetime.now().strftime('%H:%M:%S')
        
        print(f"\n🔍 Check #{attempt} at {timestamp}")
        logger.info("🌌 -" * 40)
        
        # Check DNS
        dns_ready, dns_msg = check_dns_resolution()
        print(f"DNS: {dns_msg}")
        
        # Check GitHub Pages
        if dns_ready:
            github_ready, github_msg = check_github_pages()
            print(f"GitHub Pages: {github_msg}")
            
            # Check SSL
            if github_ready:
                ssl_ready, ssl_msg = check_ssl_certificate()
                print(f"SSL: {ssl_msg}")
        else:
            logger.info("🌌 GitHub Pages: ⏳ Waiting for DNS to resolve first")
            logger.info("🌌 SSL: ⏳ Waiting for DNS to resolve first")
        
        # Status summary
        status = []
        if dns_ready: status.append("DNS ✅")
        else: status.append("DNS ❌")
        
        if github_ready: status.append("Pages ✅")
        else: status.append("Pages ❌")
        
        if ssl_ready: status.append("SSL ✅")
        else: status.append("SSL ❌")
        
        print(f"\n🎯 Status: {' | '.join(status)}")
        
        if dns_ready and github_ready and ssl_ready:
            logger.info("🌌 \n" + "🎉" * 20)
            logger.info("🌌 🚀 DONATION PORTAL IS LIVE! 🚀")
            logger.info("🌌 💎⚡ https://support.hyperfocuszone.com ⚡💎")
            logger.info("🌌 🎉" * 20)
            break
        
        if attempt < max_attempts:
            print(f"⏳ Next check in 5 seconds... ({max_attempts - attempt} attempts remaining)")
            time.sleep(5)
    
    if not (dns_ready and github_ready and ssl_ready):
        logger.info("🌌 \n⚠️  Monitoring completed but some services not ready yet.")
        logger.info("🌌 💡 This is normal - DNS can take up to 24-48 hours to fully propagate.")
        logger.info("🌌 🔄 Continue checking manually or run this script again later.")

if __name__ == "__main__":
    try:
        monitor_deployment()
    except KeyboardInterrupt:
        logger.info("🌌 \n🛑 Monitoring stopped by user")
    except Exception as e:
        print(f"\n❌ Monitoring error: {str(e)}")
