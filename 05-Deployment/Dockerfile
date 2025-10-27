FROM agrigorev/zoomcamp-model:2025

WORKDIR /app

# Copy dependency files first
COPY pyproject.toml uv.lock ./

# Install curl and uv
RUN apt-get update && apt-get install -y curl && \
    curl -LsSf https://astral.sh/uv/install.sh | sh && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install all needed Python packages
RUN pip install --no-cache-dir \
    fastapi uvicorn requests \
    numpy pandas scikit-learn joblib

# Copy your code and model
COPY main.py predict.py pipeline_v1.bin ./

EXPOSE 8000

# Run the FastAPI app
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
