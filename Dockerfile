# Use a minimal Python base image
FROM python:3.11-slim

# Install system packages including Stockfish
RUN apt-get update && apt-get install -y \
    stockfish \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy application files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Start the Flask app on the Render-assigned port
CMD ["flask", "run", "--host=0.0.0.0", "--port=$PORT"]
