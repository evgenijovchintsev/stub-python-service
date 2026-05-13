# Use official lightweight Python image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies from pyproject.toml
RUN pip install --upgrade pip && \
    pip install .

# Expose the port that uvicorn will listen on
EXPOSE 8000

# Run the application with hot reload for development
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]