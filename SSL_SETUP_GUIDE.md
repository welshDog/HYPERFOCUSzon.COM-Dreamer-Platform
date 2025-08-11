SSL CERTIFICATE SETUP GUIDE

AUTOMATIC SSL (GitHub Pages):
1. Ensure custom domain is set in GitHub Pages
2. Wait for initial certificate provisioning (up to 24 hours)
3. Verify "Enforce HTTPS" is enabled
4. Test SSL with: https://support.hyperfocuszone.com

CLOUDFLARE SSL (Additional Layer):
1. Go to SSL/TLS > Overview
2. Set encryption mode to "Full (strict)"
3. Enable "Always Use HTTPS"
4. Configure HSTS headers
5. Enable "Automatic HTTPS Rewrites"

VERIFICATION:
- SSL Labs Test: https://ssllabs.com/ssltest/
- Certificate Transparency: https://crt.sh/
