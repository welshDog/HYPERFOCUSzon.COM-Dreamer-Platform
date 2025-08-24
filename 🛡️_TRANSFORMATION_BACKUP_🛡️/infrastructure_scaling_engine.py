#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EMPIRE INFRASTRUCTURE SCALING ENGINE
HYPERFOCUS ZONE EMPIRE - Upstream Server Activation & Scaling
Target: Activate discovered server infrastructure for maximum performance
"""

import datetime
import json
import socket


def check_port_availability(host, port):
    """Check if a port is available or in use"""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(5)
            result = sock.connect_ex((host, port))
            return {
                "host": host,
                "port": port,
                "status": "IN_USE" if result == 0 else "AVAILABLE",
                "connectable": result == 0,
            }
    except Exception as e:
        return {"host": host, "port": port, "status": "ERROR", "error": str(e)}


def analyze_upstream_servers():
    """Analyze upstream server configuration and availability"""
    print("🔍 ANALYZING UPSTREAM SERVER INFRASTRUCTURE")
    print("=" * 60)

    # Server infrastructure from NGINX config
    upstream_servers = {
        "hyperfocus_app": [
            {"host": "127.0.0.1", "port": 3000, "weight": 3},
            {"host": "127.0.0.1", "port": 3001, "weight": 2},
            {"host": "127.0.0.1", "port": 3002, "weight": 2},
        ],
        "ai_cabin_services": [
            {"host": "127.0.0.1", "port": 4000, "weight": 3},
            {"host": "127.0.0.1", "port": 4001, "weight": 3},
            {"host": "127.0.0.1", "port": 4002, "weight": 2},
        ],
        "agent_army_api": [
            {"host": "127.0.0.1", "port": 5000, "weight": 3},
            {"host": "127.0.0.1", "port": 5001, "weight": 3},
            {"host": "127.0.0.1", "port": 5002, "weight": 2},
        ],
    }

    server_analysis = {}

    for service_name, servers in upstream_servers.items():
        print(f"\\n⚡ {service_name.upper()} SERVERS:")
        service_results = []

        for server in servers:
            port_check = check_port_availability(server["host"], server["port"])

            server_info = {**server, **port_check, "service": service_name}

            service_results.append(server_info)

            status_icon = "✅" if port_check["status"] == "IN_USE" else "⚠️"
            print(
                f"   {status_icon} {server['host']}:{server['port']} - Weight: {server['weight']} - {port_check['status']}"
            )

        server_analysis[service_name] = service_results

    return server_analysis


def analyze_pi_network():
    """Analyze Pi network infrastructure"""
    print("\\n🍓 ANALYZING PI NETWORK INFRASTRUCTURE")
    print("=" * 60)

    pi_network = {
        "main_dive": "100.114.5.118",
        "empire_ssh": "100.68.37.27",
        "backup": "100.71.69.16",
        "local": "192.168.137.10",
    }

    pi_analysis = {}

    for node_name, node_ip in pi_network.items():
        print(f"\\n🔍 Checking {node_name} ({node_ip})...")

        # Check SSH port (22) availability
        port_check = check_port_availability(node_ip, 22)

        network_type = "TAILSCALE" if node_ip.startswith("100.") else "LOCAL"

        pi_analysis[node_name] = {
            "ip": node_ip,
            "network_type": network_type,
            "ssh_status": port_check["status"],
            "reachable": port_check["connectable"],
        }

        status_icon = "✅" if port_check["connectable"] else "⚠️"
        print(f"   {status_icon} {node_name}: {port_check['status']} ({network_type})")

    return pi_analysis


def generate_scaling_recommendations(server_analysis, pi_analysis):
    """Generate infrastructure scaling recommendations"""
    print("\\n🚀 INFRASTRUCTURE SCALING RECOMMENDATIONS")
    print("=" * 60)

    recommendations = {
        "immediate_actions": [],
        "scaling_opportunities": [],
        "performance_improvements": [],
    }

    # Analyze server utilization
    for service_name, servers in server_analysis.items():
        available_servers = [s for s in servers if s["status"] == "AVAILABLE"]
        active_servers = [s for s in servers if s["status"] == "IN_USE"]

        print(f"\\n⚡ {service_name.upper()}:")
        print(f"   Active: {len(active_servers)}/3 servers")
        print(f"   Available: {len(available_servers)}/3 ports")

        if len(active_servers) == 0:
            recommendations["immediate_actions"].append(
                {
                    "type": "SERVER_ACTIVATION",
                    "service": service_name,
                    "action": f"Start {service_name} services on available ports",
                    "ports": [s["port"] for s in available_servers[:1]],
                    "priority": "HIGH",
                }
            )
            print(f"   🚀 RECOMMENDATION: Activate {service_name} service")

        elif len(active_servers) < 3:
            recommendations["scaling_opportunities"].append(
                {
                    "type": "HORIZONTAL_SCALING",
                    "service": service_name,
                    "action": f"Scale {service_name} from {len(active_servers)} to 3 servers",
                    "available_ports": [s["port"] for s in available_servers],
                    "priority": "MEDIUM",
                }
            )
            print(f"   📈 OPPORTUNITY: Scale {service_name} to full capacity")

    # Analyze Pi network utilization
    reachable_pis = [
        name for name, info in pi_analysis.items() if info.get("reachable", False)
    ]
    print(f"\\n🍓 PI NETWORK STATUS:")
    print(f"   Reachable nodes: {len(reachable_pis)}/4")

    if len(reachable_pis) > 0:
        recommendations["performance_improvements"].append(
            {
                "type": "PI_NETWORK_UTILIZATION",
                "action": "Leverage Pi network for distributed processing",
                "available_nodes": reachable_pis,
                "opportunity": "Distribute AI agent workloads across Pi cluster",
                "priority": "MEDIUM",
            }
        )
        print(f"   🚀 OPPORTUNITY: Utilize {len(reachable_pis)} Pi nodes for scaling")

    return recommendations


def main():
    """Execute infrastructure scaling analysis"""
    print("🚀💎⚡ EMPIRE INFRASTRUCTURE SCALING ENGINE ACTIVATED ⚡💎🚀")
    print("=" * 80)

    start_time = datetime.datetime.now()

    # Analyze current infrastructure
    server_analysis = analyze_upstream_servers()
    pi_analysis = analyze_pi_network()
    recommendations = generate_scaling_recommendations(server_analysis, pi_analysis)

    # Calculate scaling metrics
    total_servers = sum(len(servers) for servers in server_analysis.values())
    active_servers = sum(
        len([s for s in server_analysis[service] if s["status"] == "IN_USE"])
        for service in server_analysis
    )

    utilization_rate = (
        (active_servers / total_servers) * 100 if total_servers > 0 else 0
    )

    # Generate scaling report
    report_data = {
        "timestamp": start_time.strftime("%Y%m%d_%H%M%S"),
        "server_analysis": server_analysis,
        "pi_network_analysis": pi_analysis,
        "scaling_recommendations": recommendations,
        "metrics": {
            "total_configured_servers": total_servers,
            "active_servers": active_servers,
            "utilization_rate_percent": utilization_rate,
            "pi_nodes_reachable": len(
                [
                    name
                    for name, info in pi_analysis.items()
                    if info.get("reachable", False)
                ]
            ),
            "scaling_potential": (
                "HIGH"
                if utilization_rate < 50
                else "MEDIUM" if utilization_rate < 80 else "LOW"
            ),
        },
    }

    # Save scaling report
    report_file = f"infrastructure_scaling_{report_data['timestamp']}.json"
    with open(report_file, "w") as f:
        json.dump(report_data, f, indent=2, default=str)

    # Display final results
    print(f"\\n🏆 EMPIRE INFRASTRUCTURE SCALING ANALYSIS COMPLETE")
    print("=" * 60)
    print(
        f"📊 Server Utilization: {utilization_rate:.1f}% ({active_servers}/{total_servers})"
    )
    print(
        f"🍓 Pi Network: {len([name for name, info in pi_analysis.items() if info.get('reachable', False)])}/4 nodes reachable"
    )
    print(f"🎯 Scaling Potential: {report_data['metrics']['scaling_potential']}")
    print(f"📄 Report saved: {report_file}")

    # Show top recommendations
    if recommendations["immediate_actions"]:
        print(f"\\n🚀 IMMEDIATE ACTIONS AVAILABLE:")
        for action in recommendations["immediate_actions"][:3]:
            print(f"   ⚡ {action['action']} ({action['priority']} priority)")

    if recommendations["scaling_opportunities"]:
        print(f"\\n📈 SCALING OPPORTUNITIES:")
        for opportunity in recommendations["scaling_opportunities"][:3]:
            print(f"   🔧 {opportunity['action']}")

    return report_data


if __name__ == "__main__":
    main()
