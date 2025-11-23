FROM python:3.11-slim

# Install uv
RUN pip install uv

# Force uv to use Python 3.11 (critical!!)
ENV UV_PYTHON=/usr/local/bin/python3.11

WORKDIR /app

# Copy dependencies
COPY pyproject.toml uv.lock ./

# Install app dependencies
RUN uv sync --frozen --no-dev

# Copy the ingestion service code INTO /app
COPY ingestion_service/ /app/

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
