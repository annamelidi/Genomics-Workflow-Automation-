# Base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make data and figures directories
RUN mkdir -p data figures

# Default command: run the workflow script
CMD ["python", "docker.py"]
