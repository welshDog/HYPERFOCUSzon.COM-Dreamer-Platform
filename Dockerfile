# 🐳 HyperFocus Zone System Monitor - Docker Configuration
# Multi-stage build for optimized Python application containerization

# Build stage - Install dependencies and prepare application
FROM python:3.11-slim as builder

# Set build arguments for flexibility
ARG APP_VERSION=1.0.0
ARG BUILD_DATE
ARG VCS_REF

# Add metadata labels following OCI image spec
LABEL maintainer="HyperFocus Zone Empire <admin@hyperfocuszone.com>" \
    org.opencontainers.image.title="HyperFocus Zone System Monitor" \
    org.opencontainers.image.description="Real-time system performance monitoring with AI capabilities" \
    org.opencontainers.image.version="${APP_VERSION}" \
    org.opencontainers.image.created="${BUILD_DATE}" \
    org.opencontainers.image.revision="${VCS_REF}" \
    org.opencontainers.image.source="https://github.com/welshDog/HYPERFOCUSzon.COM-V10" \
    org.opencontainers.image.url="https://hyperfocuszone.com" \
    org.opencontainers.image.vendor="HyperFocus Zone Empire" \
    org.opencontainers.image.licenses="MIT"

# Set environment variables for Python optimization
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_DEFAULT_TIMEOUT=100

# Install system dependencies needed for psutil and other packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    libc6-dev \
    linux-headers-generic \
    procps \
    && rm -rf /var/lib/apt/lists/*

# Create application directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Production stage - Minimal runtime image
FROM python:3.11-slim as production

# Set runtime environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    APP_HOME=/app \
    APP_USER=appuser \
    APP_GROUP=appgroup \
    MONITORING_INTERVAL=5 \
    LOG_LEVEL=INFO \
    DATA_DIR=/app/data \
    CONFIG_DIR=/app/config

# Install only runtime system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    procps \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Create non-root user for security
RUN groupadd -r ${APP_GROUP} && \
    useradd -r -g ${APP_GROUP} -d ${APP_HOME} -s /bin/bash ${APP_USER}

# Create application directories
RUN mkdir -p ${APP_HOME} ${DATA_DIR} ${CONFIG_DIR} && \
    chown -R ${APP_USER}:${APP_GROUP} ${APP_HOME} ${DATA_DIR} ${CONFIG_DIR}

# Copy Python packages from builder stage
COPY --from=builder /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

# Set working directory
WORKDIR ${APP_HOME}

# Copy application files with proper ownership
COPY --chown=${APP_USER}:${APP_GROUP} system_monitor.py .
COPY --chown=${APP_USER}:${APP_GROUP} setup_system_monitor.py .
COPY --chown=${APP_USER}:${APP_GROUP} demo_system_monitor.py .
COPY --chown=${APP_USER}:${APP_GROUP} docker_entrypoint.sh .
COPY --chown=${APP_USER}:${APP_GROUP} config/ ${CONFIG_DIR}/

# Make entrypoint script executable
RUN chmod +x docker_entrypoint.sh

# Create health check script
RUN echo '#!/bin/bash\npython -c "from system_monitor import SystemMonitor; m=SystemMonitor(); print(\"Health: OK\")"' > /healthcheck.sh && \
    chmod +x /healthcheck.sh

# Switch to non-root user
USER ${APP_USER}

# Expose port for potential web interface (future enhancement)
EXPOSE 8080

# Add health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD /healthcheck.sh

# Create volume for persistent data
VOLUME ["${DATA_DIR}", "${CONFIG_DIR}"]

# Set entrypoint
ENTRYPOINT ["./docker_entrypoint.sh"]

# Default command
CMD ["monitor"]
