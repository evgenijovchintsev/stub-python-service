# syntax=docker/dockerfile:1
FROM python:3.13-slim AS builder
WORKDIR /app
COPY pyproject.toml .
COPY main.py config.py ./
RUN pip install --no-cache-dir -e .

FROM python:3.13-slim AS runtime
WORKDIR /app
# Copy installed dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
# Copy application source code
COPY --from=builder /app/main.py /app/config.py ./
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]