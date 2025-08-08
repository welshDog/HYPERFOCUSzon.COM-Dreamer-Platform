# 🚀💎⚡ PI MICRO-CLOUD QUICK SETUP INSTRUCTIONS ⚡💎🚀

## 🎯 STEP 1: Boot Your Pi
1. Insert this SD card into your Raspberry Pi 4
2. Connect Pi to network (Ethernet recommended for first setup)
3. Power on the Pi and wait for boot to complete
4. Enable SSH if not already enabled: `sudo systemctl enable ssh`

## 🌐 STEP 2: Find Your Pi and Connect
```bash
# Method 1: Check your router's connected devices
# Method 2: Use network scanner
# Method 3: Connect monitor and check IP with: hostname -I

# SSH into your Pi (default password: raspberry)
ssh pi@[PI_IP_ADDRESS]
```

## 📁 STEP 3: Copy Files to Pi Home Directory
```bash
# Create empire directory
mkdir -p ~/empire

# Copy pi-microcloud from boot partition to home
sudo cp -r /boot/pi-microcloud ~/empire/
sudo chown -R pi:pi ~/empire

# Navigate to deployment directory
cd ~/empire/pi-microcloud
```

## 🚀 STEP 4: Deploy Pi Micro-Cloud with Auto-Boot
```bash
# Make setup script executable
chmod +x setup-pi-microcloud.sh

# Run the complete setup (this will take 5-10 minutes)
# This installs Docker, sets up services, and configures auto-boot
./setup-pi-microcloud.sh
```

## 🧪 STEP 5: Test Your Deployment
```bash
# Check if services are running
docker ps

# Test health endpoint
curl http://localhost/health

# Check Pi status
curl http://localhost/pi/status

# Check auto-boot service
sudo systemctl status pi-microcloud
```

## 💻 STEP 6: Configure Laptop Client
1. **Find your Pi's IP address:**
   ```bash
   hostname -I
   ```

2. **Update laptop client with Pi IP:**
   - Edit `pi-microcloud-laptop-client.py`
   - Change `pi_ip = "192.168.1.100"` to your Pi's actual IP

3. **Test offloading from laptop:**
   ```python
   python pi-microcloud-laptop-client.py
   ```

## 🔄 AUTO-BOOT FEATURES INCLUDED
✅ **Pi micro-cloud starts automatically on boot**
✅ **Services restart automatically on failure**
✅ **Health monitoring enabled**
✅ **Complete logging system with rotation**
✅ **Systemd service integration**

## 🛠️ SERVICE MANAGEMENT COMMANDS
```bash
# Check auto-boot service status
sudo systemctl status pi-microcloud

# Manual service control
sudo systemctl start pi-microcloud     # Start service
sudo systemctl stop pi-microcloud      # Stop service  
sudo systemctl restart pi-microcloud   # Restart service
sudo systemctl disable pi-microcloud   # Disable auto-boot

# View service logs
sudo journalctl -u pi-microcloud -f    # Follow live logs
sudo journalctl -u pi-microcloud       # View all logs

# View application logs
tail -f /var/log/pi-microcloud.log     # Application logs
```

## 🌐 ENDPOINTS (Replace [PI_IP] with actual IP)
- **Health Check:** `http://[PI_IP]/health`
- **Pi Status:** `http://[PI_IP]/pi/status`  
- **Task Offloading:** `http://[PI_IP]/api/offload`
- **Prometheus Metrics:** `http://[PI_IP]/metrics`

## ⚡ LAPTOP OFFLOADING CAPABILITIES
Your Pi can now handle:
- 🕷️ **Web scraping tasks**
- 📊 **Data processing operations**
- 🌐 **API call batching**
- 🧮 **Background computations**
- 🧠 **BCI data analysis**
- 💾 **Caching and proxy services**
- 📊 **Distributed monitoring**

## 🚨 TROUBLESHOOTING
If setup fails:

1. **Check internet connection:**
   ```bash
   ping google.com
   ```

2. **Update system:**
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```

3. **Check Docker installation:**
   ```bash
   sudo systemctl status docker
   docker --version
   ```

4. **Check service logs:**
   ```bash
   sudo journalctl -u pi-microcloud -n 50
   ```

5. **Manual Docker start:**
   ```bash
   cd ~/empire/pi-microcloud
   docker compose up -d
   ```

6. **Test individual services:**
   ```bash
   # Test Nginx
   curl http://localhost/health
   
   # Test BROski agent
   curl http://localhost:8080/health
   
   # Test Redis
   docker exec pi-redis-cache redis-cli ping
   ```

## 🔧 MANUAL CONFIGURATION (If Auto-Boot Fails)
```bash
# Create systemd service manually
sudo tee /etc/systemd/system/pi-microcloud.service > /dev/null <<EOF
[Unit]
Description=Pi Micro-Cloud Auto-Boot Service
After=docker.service network.target
Requires=docker.service

[Service]
Type=oneshot
RemainAfterExit=yes
User=pi
WorkingDirectory=/home/pi/empire/pi-microcloud
ExecStart=/home/pi/empire/pi-microcloud/auto-start-microcloud.sh
ExecStop=/usr/bin/docker compose down
Restart=on-failure
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

# Enable the service
sudo systemctl daemon-reload
sudo systemctl enable pi-microcloud.service
sudo systemctl start pi-microcloud.service
```

## 📊 EXPECTED RESULTS
After successful deployment, you should see:

1. **Docker containers running:**
   - `pi-nginx-gateway`
   - `pi-redis-cache`
   - `pi-broski-agent`
   - `pi-node-exporter`
   - `pi-empire-sync`

2. **Service endpoints responding:**
   - Health check returns "Pi Micro-Cloud Healthy"
   - Status endpoint returns JSON with Pi metrics
   - Prometheus metrics available

3. **Auto-boot service active:**
   - `sudo systemctl status pi-microcloud` shows "active (exited)"
   - Service automatically starts on Pi reboot

## 🏆 SUCCESS INDICATORS
- ✅ `docker ps` shows 4+ containers running
- ✅ `curl http://localhost/health` returns "Pi Micro-Cloud Healthy"
- ✅ `sudo systemctl status pi-microcloud` shows "active"
- ✅ Pi automatically starts micro-cloud after reboot
- ✅ Laptop can offload tasks to Pi successfully

## 💡 PERFORMANCE TIPS
- **Monitor Pi temperature:** `vcgencmd measure_temp`
- **Check memory usage:** `free -h`
- **Monitor CPU:** `htop`
- **Check disk space:** `df -h`

## 🎊 YOU'RE READY!
Your Raspberry Pi is now a powerful micro-cloud that will:
- 🔄 **Start automatically** on every boot
- ⚡ **Handle laptop tasks** seamlessly  
- 📊 **Monitor itself** continuously
- 🛡️ **Restart services** if they fail
- 📝 **Log everything** for troubleshooting

**🚀💎⚡ Welcome to your legendary Pi micro-cloud empire! ⚡💎🚀**
