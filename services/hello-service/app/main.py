import os

from fastapi import FastAPI

app = FastAPI(title="hello-service")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": os.getenv("SERVICE_NAME", "hello-service")}


@app.get("/version")
def version() -> dict[str, str]:
    return {"version": os.getenv("SERVICE_VERSION", "0.1.0")}
