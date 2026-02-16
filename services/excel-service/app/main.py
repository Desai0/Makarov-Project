import os

from fastapi import FastAPI

app = FastAPI(title="excel-service")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": os.getenv("SERVICE_NAME", "excel-service")}


@app.get("/version")
def version() -> dict[str, str]:
    return {"version": os.getenv("SERVICE_VERSION", "0.1.0")}
