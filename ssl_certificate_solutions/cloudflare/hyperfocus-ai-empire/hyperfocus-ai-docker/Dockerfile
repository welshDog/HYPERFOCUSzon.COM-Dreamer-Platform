# HyperFocus Zone AI Assistant - Docker Image
FROM node:18-alpine

WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm ci --only=production

# Copy application code
COPY src/ ./src/

# Create non-root user
RUN addgroup -g 1001 -S hyperfocus && adduser -S hyperfocus -u 1001 -G hyperfocus
RUN chown -R hyperfocus:hyperfocus /app
USER hyperfocus

# Expose port
EXPOSE 8888

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8888/health || exit 1

# Start application
CMD ["node", "src/server.js"]
