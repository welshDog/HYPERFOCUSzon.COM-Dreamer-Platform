# 🏆💎⚡ HYPERFOCUS AZURE EMPIRE - DOCKERFILE ⚡💎🏆
# Legendary containerization for 9,437 Python modules
# Ultimate AI empire ready for Azure Container Apps

FROM python:3.11-slim

# 🎯 Set working directory for empire operations
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Streamlit application
COPY 🚀💎⚡_BROSKIE_ULTRA_AGENT_LAB_CONTROL_PANEL_⚡💎🚀.py app.py

# Expose Streamlit port
EXPOSE 8501

# Health check
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health || exit 1

# Create non-root user for security
RUN useradd --create-home --shell /bin/bash broskie
USER broskie

# Run Streamlit application
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.headless=true", "--server.enableCORS=false", "--server.enableXsrfProtection=false"]
