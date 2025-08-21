# SSL Certificate Verification

## Tools
- verify_ssl.py - Detailed certificate verification
- quick_test.sh - Quick connectivity test

## Usage
```bash
python3 verify_ssl.py
chmod +x quick_test.sh && ./quick_test.sh
```

## Expected Results
When SSL is properly configured:
- All domains show "OK - Valid certificate covers domain"
- No hostname mismatch errors
- All HTTPS connections succeed

## Troubleshooting
- Certificate errors: Check SAN list includes all domains
- Connection failures: Check DNS and firewall
- Hostname mismatch: Update certificate with correct SAN
