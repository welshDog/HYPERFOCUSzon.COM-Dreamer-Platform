#!/usr/bin/env python3
"""
✅💎⚡ SSL VERIFICATION TOOL ⚡💎✅
HYPERFOCUS ZONE EMPIRE - Quick SSL Certificate Verification
Target: Verify support.hyperfocuszone.com SSL fix
"""

import datetime
import socket
import ssl


def quick_ssl_check(domain, port=443):
    """Quick SSL certificate check for a domain"""
    try:
        print(f"🔍 Checking SSL certificate for {domain}...")

        context = ssl.create_default_context()
        with socket.create_connection((domain, port), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()

                # Get certificate details
                subject = dict(x[0] for x in cert["subject"])
                issuer = dict(x[0] for x in cert["issuer"])

                # Parse dates
                not_before = datetime.datetime.strptime(
                    cert["notBefore"], "%b %d %H:%M:%S %Y %Z"
                )
                not_after = datetime.datetime.strptime(
                    cert["notAfter"], "%b %d %H:%M:%S %Y %Z"
                )
                now = datetime.datetime.now()
                days_until_expiry = (not_after - now).days

                # Check SAN (Subject Alternative Names)
                san_list = []
                for extension in cert.get("subjectAltName", []):
                    if extension[0] == "DNS":
                        san_list.append(extension[1])

                return {
                    "status": "VALID",
                    "subject_cn": subject.get("commonName", "N/A"),
                    "issuer_name": issuer.get("organizationName", "N/A"),
                    "issuer_cn": issuer.get("commonName", "N/A"),
                    "valid_from": not_before.strftime("%Y-%m-%d %H:%M:%S"),
                    "valid_until": not_after.strftime("%Y-%m-%d %H:%M:%S"),
                    "days_until_expiry": days_until_expiry,
                    "is_valid": not_before <= now <= not_after,
                    "san_list": san_list,
                    "domain_in_san": domain in san_list
                    or domain == subject.get("commonName"),
                }

    except Exception as e:
        return {
            "status": "ERROR",
            "error": str(e),
            "domain_in_san": False,
        }


def verify_ssl_fix():
    """Verify SSL certificate fix for support.hyperfocuszone.com"""
    print("✅💎⚡ SSL VERIFICATION TOOL ACTIVATED ⚡💎✅")
    print("=" * 60)

    # Check support.hyperfocuszone.com specifically
    domain = "support.hyperfocuszone.com"
    result = quick_ssl_check(domain)

    print(f"\n🎯 SSL VERIFICATION FOR {domain}:")
    print("=" * 50)

    if result["status"] == "VALID":
        print("✅ SSL Certificate Status: VALID")
        print(f"🔒 Subject CN: {result['subject_cn']}")
        print(f"🏢 Issuer: {result['issuer_name']} ({result['issuer_cn']})")
        print(f"📅 Valid From: {result['valid_from']}")
        print(f"📅 Valid Until: {result['valid_until']}")
        print(f"⏰ Days Until Expiry: {result['days_until_expiry']}")

        print(f"\n📋 Subject Alternative Names (SAN):")
        if result["san_list"]:
            for san in result["san_list"]:
                print(f"   🌐 {san}")
        else:
            print("   ⚠️ No SAN entries found")

        if result["domain_in_san"]:
            print(f"\n🎉 SUCCESS: {domain} is covered by the certificate!")
            print("✅ SSL certificate hostname mismatch issue RESOLVED!")
            return True
        else:
            print(f"\n❌ ISSUE: {domain} is NOT covered by the certificate")
            print("⚠️ SSL certificate hostname mismatch issue still exists")
            return False

    else:
        print("❌ SSL Certificate Status: ERROR")
        print(f"🚨 Error: {result['error']}")
        print("⚠️ SSL certificate issue still exists")
        return False


def check_all_subdomains():
    """Check SSL status for all HYPERFOCUS ZONE subdomains"""
    print("\n🌐 COMPREHENSIVE SSL STATUS CHECK:")
    print("=" * 45)

    domains = [
        "hyperfocuszone.com",
        "www.hyperfocuszone.com",
        "support.hyperfocuszone.com",
        "api.hyperfocuszone.com",
        "admin.hyperfocuszone.com",
    ]

    results = {}
    all_valid = True

    for domain in domains:
        result = quick_ssl_check(domain)
        results[domain] = result

        if result["status"] == "VALID" and result["domain_in_san"]:
            print(f"✅ {domain}: SSL Valid & Covered")
        elif result["status"] == "VALID":
            print(f"⚠️ {domain}: SSL Valid but NOT Covered by Certificate")
            all_valid = False
        else:
            print(f"❌ {domain}: SSL Error - {result.get('error', 'Unknown error')}")
            all_valid = False

    print(f"\n🏆 OVERALL SSL STATUS:")
    if all_valid:
        print("🎊 ALL SUBDOMAINS HAVE VALID SSL CERTIFICATES!")
        print("💎 HYPERFOCUS ZONE SSL INFRASTRUCTURE: 100% OPERATIONAL")
    else:
        print("🔧 Some SSL issues remain - check individual domain status above")

    return all_valid, results


def main():
    """Main SSL verification execution"""
    try:
        # Verify specific support subdomain fix
        support_fixed = verify_ssl_fix()

        # Check all subdomains
        all_valid, all_results = check_all_subdomains()

        # Generate summary
        print(f"\n📊 SSL VERIFICATION SUMMARY:")
        print("=" * 40)
        print(
            f"🎯 Support Subdomain Fix: {'✅ RESOLVED' if support_fixed else '❌ NEEDS ACTION'}"
        )
        print(
            f"🌐 All Subdomains Status: {'✅ ALL VALID' if all_valid else '⚠️ ISSUES REMAIN'}"
        )

        if support_fixed:
            print(f"\n🚀 NEXT STEPS:")
            print(f"   ✅ support.hyperfocuszone.com SSL is now working!")
            print(f"   🔄 Update any applications using the support subdomain")
            print(f"   📊 Monitor SSL certificate expiration")
            print(f"   🎊 Celebrate successful SSL fix!")
        else:
            print(f"\n🔧 NEXT STEPS:")
            print(f"   1. Implement SSL certificate fix (Option 1 recommended)")
            print(f"   2. Add support.hyperfocuszone.com to certificate SAN")
            print(f"   3. Re-deploy certificate to server")
            print(f"   4. Run this verification tool again")

        return {
            "support_fixed": support_fixed,
            "all_valid": all_valid,
            "results": all_results,
        }

    except Exception as e:
        print(f"❌ SSL Verification Error: {str(e)}")
        return None


if __name__ == "__main__":
    main()
