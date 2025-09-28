# Use a lightweight Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Optional: expose port if using Flask API later
EXPOSE 5000

# Run the pipeline
CMD ["python", "main.py"]


# Build the image
docker build -t threat-detector .

# Run the container
docker run --rm threat-detector
