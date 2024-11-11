FROM python:3.8

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy start script first and set permissions
COPY start.sh /app/
RUN chmod +x /app/start.sh

# Copy project files
COPY . .

# Set proper permissions for the app directory
RUN chown -R www-data:www-data /app

# Expose port
EXPOSE 8000

# Command to run the application
ENTRYPOINT ["/bin/bash", "/app/start.sh"]