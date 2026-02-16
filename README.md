# Course Platform (Monorepo)

Monorepository for the course: separate services + infrastructure + documentation.

## Structure
- `services/` - microservices (each service is an isolated module)
- `infra/` - infrastructure (`gateway`, `monitoring`)
- `compose/` - compose files for environments (dev/prod)
- `docs/` - documentation and project notes

## Base Rules
- All changes go through Pull Requests.
- Every service must expose `/health` and `/version`.
- Configuration is provided through environment variables.
