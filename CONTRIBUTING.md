# Contributing

## How We Submit Tasks
1. Create a branch from `main`:
   `git checkout -b feat/<short-task-name>`
2. Make changes and verify startup/build locally.
3. Create meaningful commits:
   - `feat: ...`
   - `fix: ...`
   - `docs: ...`
   - `chore: ...`
4. Push the branch and open a Pull Request into `main`.

## Service Standards
Every service must provide:
- `/health`
- `/version`
- `Dockerfile`
- `.env.example`
- `README.md` with run instructions

## Forbidden
- Pushing secrets (`.env`)
- Breaking common repository structure without agreement
- Working directly in `main`
