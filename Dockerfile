FROM python:3.13-slim

WORKDIR /app

# Install system dependencies for optional packages (e.g., PostgreSQL driver)
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Upgrade pip and install project dependencies from pyproject.toml
COPY pyproject.toml .
RUN pip install --upgrade pip && \
    pip install .

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copy the rest of the application code
COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]