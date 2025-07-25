# FastAPI OCR Service

This repository contains a Dockerized FastAPI service exposing an OCR API that uses the [Surya OCR](https://github.com/datalab-to/surya) library and a PostgreSQL database for storing inputs and metadata.

## Setup

Install Python dependencies for local development:

```bash
pip install -r requirements.txt
```

Alternatively, build the Docker image:

```bash
docker compose build
```

## Running the service

Start the stack using Docker Compose which will launch the API and a PostgreSQL instance:

```bash
docker compose up
```

The API will be available on `http://localhost:5000`.

## Testing

Run unit tests with:

```bash
pytest
```
