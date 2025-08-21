#!/usr/bin/env python3
"""
SSL Certificate Verification
"""
import socket
import ssl
import datetime

def check_ssl(domain):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()

                subject = dict(x[0] for x in cert['subject'])
                not_after = datetime.datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
                days_left = (not_after - datetime.datetime.now()).days

                san_list = []
                for ext in cert.get('subjectAltName', []):
                    if ext[0] == 'DNS':
                        san_list.append(ext[1])

                covered = domain in san_list or domain == subject.get('commonName')

                return {
                    'status': 'VALID',
                    'covered': covered,
                    'days_left': days_left,
                    'subject': subject.get('commonName', 'N/A'),
                    'san_list': san_list
                }
    except Exception as e:
        return {
            'status': 'ERROR',
            'error': str(e),
            'covered': False
        }

def main():
    print("SSL CERTIFICATE VERIFICATION")
    print("=" * 40)

    domains = ['hyperfocuszone.com', 'www.hyperfocuszone.com', 'support.hyperfocuszone.com', 'api.hyperfocuszone.com', 'admin.hyperfocuszone.com']
    all_good = True

    for domain in domains:
        print(f"\nChecking {domain}...")
        result = check_ssl(domain)

        if result['status'] == 'VALID' and result['covered']:
            print(f"   OK - Valid certificate covers {domain}")
            print(f"        Expires in {result['days_left']} days")
        elif result['status'] == 'VALID':
            print(f"   ERROR - Certificate does NOT cover {domain}")
            print(f"           Certificate is for: {result['subject']}")
            all_good = False
        else:
            print(f"   ERROR - {result['error']}")
            all_good = False

    print(f"\n" + "=" * 40)
    if all_good:
        print("SUCCESS: All certificates valid and properly configured!")
        print("SSL hostname mismatch issue RESOLVED!")
    else:
        print("ISSUES FOUND: Check certificate configuration")

    return all_good

if __name__ == "__main__":
    main()
