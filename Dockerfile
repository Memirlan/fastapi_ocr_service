# Use NVIDIA CUDA runtime
FROM nvcr.io/nvidia/pytorch:24.01-py3

# Install Python and dependencies
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv libgl1

WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy application code
COPY app /app/app

# Set environment variables
ENV TORCH_DEVICE=cuda
ENV PYTHONUNBUFFERED=1

# Expose port
EXPOSE 5000

# Start the server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]
