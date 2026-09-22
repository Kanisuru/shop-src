# syntax=docker/dockerfile:1
FROM python:3.12-slim AS base
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM base AS test
COPY . .
RUN python -m pip install pytest && pytest -q

FROM python:3.12-slim
WORKDIR /app
RUN useradd --create-home --uid 10001 appuser
COPY --from=base /usr/local/lib/python3.12 /usr/local/lib/python3.12
COPY --from=base /usr/local/bin /usr/local/bin
COPY app.py .
USER 10001
EXPOSE 8080
ENV PYTHONUNBUFFERED=1
CMD ["python", "app.py"]
