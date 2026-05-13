FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Install dependencies and copy project files
COPY . .
RUN pip install --no-cache-dir -e .

# Expose application port
EXPOSE 8000

# Run FastAPI with hot reload
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]