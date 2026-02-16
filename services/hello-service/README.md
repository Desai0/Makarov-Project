# hello-service

## Run locally
```bash
uv pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Endpoints:
- `/health`
- `/version`
