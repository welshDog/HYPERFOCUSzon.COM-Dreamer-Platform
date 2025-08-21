#!/bin/bash
# Generate Let's Encrypt Certificate

sudo certbot --nginx \
    -d hyperfocuszone.com -d www.hyperfocuszone.com -d support.hyperfocuszone.com -d api.hyperfocuszone.com -d admin.hyperfocuszone.com \
    --agree-tos \
    --non-interactive \
    --redirect \
    --email admin@hyperfocuszone.com

# Setup auto-renewal
(crontab -l 2>/dev/null; echo "0 12 * * * /usr/bin/certbot renew --quiet") | crontab -

echo "SUCCESS: SSL certificate generated and auto-renewal configured!"
