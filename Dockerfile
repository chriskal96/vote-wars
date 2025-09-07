# Use official lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system deps needed for psycopg2 and build tools
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Make poetry available on PATH
ENV PATH="/root/.local/bin:$PATH"

# Disable Poetry creating virtualenvs inside container
RUN poetry config virtualenvs.create false

# Copy only dependency files first (to leverage Docker layer caching)
COPY pyproject.toml poetry.lock* /app/

# Install dependencies (including psycopg2-binary)
RUN poetry install --no-root --no-interaction --no-ansi

# Now copy the actual app source
COPY . /app

# Expose FastAPI port
EXPOSE 8000

# Run the app with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
