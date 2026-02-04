FROM python:3.13.9-slim

WORKDIR /app

# Copiar pyproject y poetry.lock
COPY pyproject.toml poetry.lock /app/

# Instalar Poetry y dependencias
RUN pip install --upgrade pip \
    && pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --only=main,api,ai --no-root

# Copiar código
COPY src ./src
COPY dashboard ./dashboard

EXPOSE 8000

# CMD default (desarrollo)
CMD ["uvicorn", "autometrics.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
