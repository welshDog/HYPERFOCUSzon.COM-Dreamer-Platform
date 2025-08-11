DNS CNAME SETUP INSTRUCTIONS

1. Log into Cloudflare Dashboard
2. Navigate to DNS > Records
3. Add CNAME record:
   - Name: support
   - Target: welshdog.github.io
   - TTL: Auto
   - Proxy Status: DNS Only (gray cloud)

4. Verify GitHub Pages settings:
   - Repository: HYPERFOCUSzone-Community
   - Source: Deploy from branch (main)
   - Custom domain: support.hyperfocuszone.com
   - Enforce HTTPS: Enabled

5. Wait for propagation (up to 24 hours)
