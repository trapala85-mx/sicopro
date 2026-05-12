# Agent Guidance - sicopro

## Developer Commands

### Backend (Django)
- All commands are executed inside ```backend/``` folder.
- Run management commands: `uv run python manage.py <command>`
- Run tests: `uv run python manage.py test`
- Create apps: `uv run python manage.py djapp <app_name>`

### Frontend (React + Vite)
- All commands are executed inside ```frontend/``` folder.
- Install dependencies: `npm install`
- Start development server: `npm run dev`
- Run linter: `npm run lint`
- Build for production: `npm run build`

## Architecture

- **Full-stack**: Split into `backend/` and `frontend/` directories.
- **Backend**: 
    - Framework: Django with Django REST Framework (DRF).
    - Package Manager: `uv` (refer to `backend/pyproject.toml` and `backend/uv.lock`).
    - Apps: Located in `backend/apps/` (e.g., `core`, `launcher`).
    - Settings: Modularized in `backend/config/settings/` (base, local, prod, etc.).
- **Frontend**:
    - Framework: React 19 with TypeScript and Vite.
    - Tooling: ESLint for linting.

## Conventions

- **Backend Apps**: New Django apps should be created within `backend/apps/`. The `djapp` command already does this.
- **Frontend**: All frontend code resides in the `frontend/` directory.
- **Testing**: Backend tests are located in `tests.py` (core) or `tests/` directory (launcher).
