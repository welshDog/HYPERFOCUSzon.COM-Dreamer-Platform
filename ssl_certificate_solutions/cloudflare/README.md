# Cloudflare SSL Solution

## Quick Start
1. Get Cloudflare API token: https://dash.cloudflare.com/profile/api-tokens
2. Set environment variable: export CLOUDFLARE_API_TOKEN="your_token"
3. Run: python3 setup.py
4. Run: chmod +x deploy.sh && ./deploy.sh

## What it does
- Creates FREE SSL certificate covering all subdomains
- Includes support.hyperfocuszone.com in certificate SAN
- Deploys to server automatically
- Zero ongoing costs

## Requirements
- Domain on Cloudflare DNS
- Cloudflare API token
- SSH access to server

## Benefits
- FREE forever
- Automatic renewal by Cloudflare
- Instant certificate generation
- No certificate authority fees
