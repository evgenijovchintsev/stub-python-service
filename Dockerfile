FROM python:3.13-slim

WORKDIR /app

# Install Python dependencies
RUN pip install --no-cache-dir \
    fastapi>=0.115 \
    uvicorn[standard]>=0.30 \
    sqlalchemy>=2.0 \
    asyncpg>=0.29 \
    alembic>=1.13 \
    pydantic>=2.0 \
    pyjwt>=2.8 \
    passlib[bcrypt]>=1.7 \
    pydantic-settings>=2.14.1

# Copy source code into container
COPY . .

# Ensure output is sent straight to terminal (no buffering)
ENV PYTHONUNBUFFERED=1

# Run the application with hot reload enabled for development
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]