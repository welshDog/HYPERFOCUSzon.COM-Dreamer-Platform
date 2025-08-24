#!/bin/bash
# MinIO Empire Storage Initialization Script

echo "🗄️  Initializing MinIO Empire Storage..."

# Wait for MinIO to start
sleep 10

# Configure MinIO client
mc alias set empire http://localhost:9000 empire_access_key legendary_secret_key

# Create empire buckets
echo "📦 Creating empire buckets..."
mc mb empire/empire-data
mc mb empire/empire-logs
mc mb empire/empire-backups
mc mb empire/empire-metrics
mc mb empire/empire-assets

# Set bucket policies
echo "🔐 Setting bucket policies..."
mc policy set public empire/empire-assets
mc policy set private empire/empire-data
mc policy set private empire/empire-logs
mc policy set private empire/empire-backups
mc policy set private empire/empire-metrics

# Create lifecycle rules
echo "♻️  Setting up lifecycle management..."
mc ilm add --expiry-days 30 empire/empire-logs
mc ilm add --expiry-days 90 empire/empire-backups

echo "✅ MinIO Empire Storage initialized successfully!"
