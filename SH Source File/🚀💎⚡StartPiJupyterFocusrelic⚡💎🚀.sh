#!/bin/bash
# 🔥💎⚡ LEGENDARY PI JUPYTER STARTUP SCRIPT ⚡💎🔥
# 
# This script starts Jupyter Notebook on the Raspberry Pi
# for legendary Pi-Laptop development fusion!

echo "🚀 STARTING LEGENDARY JUPYTER ON RASPBERRY PI..."
echo "🎯 Pi IP: 192.168.137.10"
echo "📓 Jupyter will be available at: http://192.168.137.10:8888"
echo ""

# Start Jupyter Notebook with configuration for Pi-Laptop access
jupyter notebook \
    --ip=0.0.0.0 \
    --port=8888 \
    --no-browser \
    --allow-root \
    --NotebookApp.token='' \
    --NotebookApp.password='' \
    --NotebookApp.allow_origin='*' \
    --NotebookApp.disable_check_xsrf=True

echo "🎊 JUPYTER NOTEBOOK STARTED ON PI!"
echo "🌐 Access from laptop: http://192.168.137.10:8888"
echo "🔥💎⚡ LEGENDARY PI-LAPTOP FUSION READY! ⚡💎🔥"
