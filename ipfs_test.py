#!/usr/bin/env python3
"""
Simple IPFS Portal Deployer
"""

import requests
import json
import time

def test_pinata():
    """Test Pinata connection"""
    jwt = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiI0YWE3YWQ5Yi05MzBhLTQ0YjYtOTdlYS1hNjc5OGU1MjFiZTQiLCJlbWFpbCI6Imx5bmR6d2lsbHNAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInBpbl9wb2xpY3kiOnsicmVnaW9ucyI6W3siZGVzaXJlZFJlcGxpY2F0aW9uQ291bnQiOjEsImlkIjoiTllDMSJ9XSwidmVyc2lvbiI6MX0sIm1mYV9lbmFibGVkIjpmYWxzZSwic3RhdHVzIjoiQUNUSVZFIn0sImF1dGhlbnRpY2F0aW9uVHlwZSI6InNjb3BlZEtleSIsInNjb3BlZEtleUtleSI6IjhlNjIxMGMwZjBlNGVlMDEzNmVmIiwic2NvcGVkS2V5U2VjcmV0IjoiMjgwNDUyNmYxMmQ5NmZjODljOWVkMWNmYWIwZjdkZDU0MGUyODQ5NjU4ODU2MjQ3ZjlhMzc3OWNkNWY1MmQ2ZiIsImV4cCI6MTc4NDc3NTcwMn0.xL-_PvK6cy6b_xHopcf6OiKIG1po-T0v5FckLd2V6tE"
    
    headers = {
        'Authorization': f'Bearer {jwt}'
    }
    
    try:
        response = requests.get('https://api.pinata.cloud/data/testAuthentication', headers=headers)
        print(f"Pinata Auth Test: {response.status_code}")
        if response.status_code == 200:
            print("SUCCESS: Pinata connected!")
            print(f"Response: {response.json()}")
            return True
        else:
            print(f"ERROR: {response.text}")
            return False
    except Exception as e:
        print(f"ERROR: {e}")
        return False

def upload_simple_file():
    """Upload a simple test file to IPFS"""
    jwt = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiI0YWE3YWQ5Yi05MzBhLTQ0YjYtOTdlYS1hNjc5OGU1MjFiZTQiLCJlbWFpbCI6Imx5bmR6d2lsbHNAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInBpbl9wb2xpY3kiOnsicmVnaW9ucyI6W3siZGVzaXJlZFJlcGxpY2F0aW9uQ291bnQiOjEsImlkIjoiTllDMSJ9XSwidmVyc2lvbiI6MX0sIm1mYV9lbmFibGVkIjpmYWxzZSwic3RhdHVzIjoiQUNUSVZFIn0sImF1dGhlbnRpY2F0aW9uVHlwZSI6InNjb3BlZEtleSIsInNjb3BlZEtleUtleSI6IjhlNjIxMGMwZjBlNGVlMDEzNmVmIiwic2NvcGVkS2V5U2VjcmV0IjoiMjgwNDUyNmYxMmQ5NmZjODljOWVkMWNmYWIwZjdkZDU0MGUyODQ5NjU4ODU2MjQ3ZjlhMzc3OWNkNWY1MmQ2ZiIsImV4cCI6MTc4NDc3NTcwMn0.xL-_PvK6cy6b_xHopcf6OiKIG1po-T0v5FckLd2V6tE"
    
    # Create a simple test HTML file
    test_content = """<!DOCTYPE html>
<html>
<head>
    <title>IMMORTAL HYPERFOCUS EMPIRE - IPFS Test</title>
    <meta charset="UTF-8">
</head>
<body>
    <h1>🎊 IMMORTAL HYPERFOCUS EMPIRE 🎊</h1>
    <h2>IPFS Deployment Test - SUCCESS!</h2>
    <p>Portal Type: Web3 News Portal</p>
    <p>Status: IMMORTAL ♾️</p>
    <p>Deployment Time: """ + time.strftime("%Y-%m-%d %H:%M:%S UTC") + """</p>
    <style>
        body { 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white; 
            font-family: Arial, sans-serif; 
            text-align: center; 
            padding: 50px;
        }
        h1 { font-size: 3em; margin-bottom: 20px; }
        h2 { color: #ffeb3b; }
    </style>
</body>
</html>"""
    
    headers = {
        'Authorization': f'Bearer {jwt}'
    }
    
    files = {
        'file': ('index.html', test_content, 'text/html')
    }
    
    metadata = {
        'name': 'IMMORTAL_HYPERFOCUS_EMPIRE_TEST',
        'keyvalues': {
            'empire_type': 'Web3_Portal_Test',
            'status': 'IMMORTAL',
            'deployment_time': str(int(time.time()))
        }
    }
    
    data = {
        'pinataMetadata': json.dumps(metadata),
        'pinataOptions': json.dumps({'cidVersion': 1})
    }
    
    try:
        print("Uploading test file to IPFS...")
        response = requests.post(
            'https://api.pinata.cloud/pinning/pinFileToIPFS',
            files=files,
            data=data,
            headers=headers,
            timeout=60
        )
        
        if response.status_code == 200:
            result = response.json()
            ipfs_hash = result.get('IpfsHash')
            
            print("🎊 SUCCESS: File uploaded to IPFS!")
            print(f"IPFS Hash: {ipfs_hash}")
            print(f"Access URL: https://gateway.pinata.cloud/ipfs/{ipfs_hash}")
            print(f"Backup URL: https://cloudflare-ipfs.com/ipfs/{ipfs_hash}")
            
            # Save result
            with open('h:/ipfs_test_result.json', 'w') as f:
                json.dump(result, f, indent=2)
            
            print("Result saved to: h:/ipfs_test_result.json")
            return result
            
        else:
            print(f"ERROR: Upload failed: {response.status_code}")
            print(f"Response: {response.text}")
            return None
            
    except Exception as e:
        print(f"ERROR: Upload error: {e}")
        return None

def main():
    print("IMMORTAL HYPERFOCUS EMPIRE - IPFS TEST")
    print("=" * 50)
    
    # Test connection
    if test_pinata():
        print("\n" + "=" * 50)
        # Upload test file
        result = upload_simple_file()
        
        if result:
            print("\n" + "=" * 50)
            print("🏆 ACHIEVEMENT UNLOCKED: IPFS DEPLOYMENT SUCCESS!")
            print("Your portal is now IMMORTAL on the decentralized web!")
            print("=" * 50)
        else:
            print("\n❌ Upload failed - check logs")
    else:
        print("\n❌ Pinata connection failed")

if __name__ == "__main__":
    main()
