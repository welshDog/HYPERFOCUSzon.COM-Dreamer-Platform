#!/usr/bin/env python3
"""
🔧🏆⚡ LEGENDARY NETWORK RECOVERY MONITOR ⚡🏆🔧

Continuously monitors network connectivity and executes recovery when available
"""

from datetime import datetime
import subprocess
import time
def log_status(message, status="INFO"):
    timestamp = datetime.now().strftime("%H:%M:%S")
    symbols = {"INFO": "ℹ️", "SUCCESS": "✅", "WARNING": "⚠️", "ERROR": "❌", "RECOVERY": "🔧"}
    print(f"{symbols.get(status, 'ℹ️')} [{timestamp}] {message}")

def check_tailscale_status():
    """Check if target server is online in Tailscale mesh"""
    try:
        result = subprocess.run(['tailscale', 'status'], capture_output=True, text=True)
        if result.returncode == 0:
            for line in result.stdout.split('\n'):
                if '100.68.37.27' in line and 'ubuntu' in line:
                    if 'offline' in line:
                        return False, "Server offline in Tailscale mesh"
                    else:
                        return True, "Server online in Tailscale mesh"
        return False, "Server not found in Tailscale status"
    except Exception as e:
        return False, f"Tailscale check error: {e}"

def check_ssh_connectivity():
    """Test SSH connectivity to target server"""
    try:
        result = subprocess.run([
            'powershell',
            'Test-NetConnection -ComputerName 100.68.37.27 -Port 22 -InformationLevel Quiet'
        ], capture_output=True, text=True)
        return result.stdout.strip() == 'True', result.stdout.strip()
    except Exception as e:
        return False, f"SSH test error: {e}"

def execute_recovery():
    """Execute the recovery sequence when connectivity is restored"""
    log_status("🚀 CONNECTIVITY RESTORED - EXECUTING RECOVERY SEQUENCE!", "SUCCESS")

    recovery_commands = [
        "# 🔧 Starting Legendary Recovery Sequence",
        'ssh root@100.68.37.27 "echo \\"🏆 SSH Connection Established\\""',
        'ssh root@100.68.37.27 "systemctl status tailscaled"',
        'ssh root@100.68.37.27 "tailscale status"',
        '# 🧹 Clean previous installation',
        'ssh root@100.68.37.27 "kubeadm reset --force 2>/dev/null || true"',
        'ssh root@100.68.37.27 "systemctl stop kubelet containerd 2>/dev/null || true"',
        'ssh root@100.68.37.27 "rm -rf /etc/kubernetes/* /var/lib/etcd/* /etc/cni/net.d/* 2>/dev/null || true"',
        'ssh root@100.68.37.27 "iptables -F && iptables -t nat -F && iptables -t mangle -F && iptables -X 2>/dev/null || true"',
        '# 🚀 Start services',
        'ssh root@100.68.37.27 "systemctl start containerd && systemctl start kubelet"',
        '# ⏳ Wait for services',
        'Start-Sleep 10',
        '# ☸️ Initialize cluster',
        'ssh root@100.68.37.27 "kubeadm init --apiserver-advertise-address=100.68.37.27 --pod-network-cidr=10.244.0.0/16 --ignore-preflight-errors=all"'
    ]

    log_status("💎 Recovery commands prepared - Execute manually when ready", "RECOVERY")
    for cmd in recovery_commands:
        print(f"    {cmd}")

    return True

def main():
    """Main monitoring loop"""
    print("""
🔧🏆⚡ LEGENDARY NETWORK RECOVERY MONITOR ⚡🏆🔧
==================================================

👀 Monitoring network connectivity to server 100.68.37.27
🎯 Will execute recovery sequence when connectivity restored
⏰ Check interval: 30 seconds
    """)

    consecutive_failures = 0
    last_status = None

    while True:
        try:
            # Check Tailscale status
            ts_online, ts_msg = check_tailscale_status()

            # Check SSH connectivity
            ssh_online, ssh_msg = check_ssh_connectivity()

            current_status = f"Tailscale: {'✅' if ts_online else '❌'} | SSH: {'✅' if ssh_online else '❌'}"

            if current_status != last_status:
                log_status(f"Status Update: {current_status}")
                log_status(f"  Tailscale: {ts_msg}")
                log_status(f"  SSH: {ssh_msg}")
                last_status = current_status

            if ts_online and ssh_online:
                log_status("🎉 FULL CONNECTIVITY RESTORED!", "SUCCESS")
                execute_recovery()
                log_status("🏆 Recovery sequence ready - execute the displayed commands", "SUCCESS")
                break
            else:
                consecutive_failures += 1
                if consecutive_failures % 10 == 0:  # Every 5 minutes
                    log_status(f"Still waiting... ({consecutive_failures * 30}s elapsed)", "WARNING")

            time.sleep(30)

        except KeyboardInterrupt:
            log_status("🛑 Monitoring stopped by user", "WARNING")
            break
        except Exception as e:
            log_status(f"Monitor error: {e}", "ERROR")
            time.sleep(30)

if __name__ == "__main__":
    main()
