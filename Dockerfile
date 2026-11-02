# imagen base con python 3.12
FROM python:3.12-slim

# traemos uv desde su imagen oficial
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# primero las dependencias, asi docker las reusa si no cambian
COPY pyproject.toml uv.lock .python-version ./
RUN uv sync --locked

# despues el codigo
COPY . .

WORKDIR /app/src
EXPOSE 8000

# migra y levanta el servidor escuchando desde afuera del contenedor
CMD ["sh", "-c", "uv run manage.py migrate && uv run manage.py runserver 0.0.0.0:8000"]
