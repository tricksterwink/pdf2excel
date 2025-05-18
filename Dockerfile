FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    FLASK_APP=run.py \
    FLASK_ENV=production

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    ghostscript \
    tesseract-ocr \
    poppler-utils \
    libmagic1 \
    libmagic-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables for Ghostscript
ENV PATH="/usr/bin/gs:${PATH}"
ENV GHOSTSCRIPT_LIB="/usr/lib/ghostscript"
ENV GHOSTSCRIPT_RESOURCE="/usr/share/ghostscript"

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create necessary directories with proper permissions
RUN mkdir -p /app/uploads /tmp/pdf2excel && \
    chmod -R 777 /app/uploads /tmp/pdf2excel

# Set working directory and ensure proper permissions
WORKDIR /app
RUN chmod -R 777 /app

# Expose port
EXPOSE 8080

# Set the user to a non-root user
RUN useradd -m appuser && \
    chown -R appuser:appuser /app
USER appuser

# Run the application with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--timeout", "120", "--workers", "2", "--threads", "4", "--worker-class", "gthread", "run:app"]