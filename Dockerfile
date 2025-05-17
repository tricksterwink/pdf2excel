# Use official Python image
FROM python:3.13-bookworm

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y build-essential ghostscript python3-dev libglib2.0-0 libsm6 libxext6 libxrender-dev poppler-utils xvfb && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project
COPY . /app/

# Expose port
EXPOSE 8080

# Run the application
CMD ["xvfb-run", "-a", "python", "run.py"]
