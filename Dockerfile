# Use official slim image with Python 3.11
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies (optional but useful for some packages)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source code
COPY . .

# Expose port (for clarity/documentation)
EXPOSE 8000

# Run the FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
