# Amazon Price Tracker (Portfolio Version)

This repository is a **portfolio-friendly** version of an Amazon price-tracking system.
It is intentionally *partial* — core architecture, data models, examples, and various code
snippets are included in this showcase without exposing a production-ready scraper.

## Disclaimer:
Various files have been deliberately alterer to not contain production scraping logic, or credentials. They are intended to show architecture and flow.

## Brief
Build a system to monitor product prices and notify users when a price drops.

## Architecture (high level)
- Fetcher (HTTP) -> Parser (HTML -> data) -> Tracker (Core logic) -> DB (Postgres) -> Notifier (Discord)
- Background scheduler triggers tracker for all products (hourly)
- FastAPI provides CRUD endpoints to manage products

## Key Design Decisions
1. **Store money as integers (penny)** to avoid floating point rounding errors.
2. **Decouple responsibilities**: fetch, parse, and notify are separate modules for testability.
3. **Async everywhere**: uses async HTTP client and async DB sessions for scalability.
4. **Observability**: structured logs and clear timestamps for debugging and audit.

## What this contains
- `app/models.py` — SQLAlchemy model snippets.
- `app/scraper/parser.py` — safe, simple price parsing function.
- `app/services/notifier.py` — example Discord notifier (code snippet).
- `app/scraper/fetcher.py` — pseudocode placeholder (networking/scraping removed).
- `app/services/tracker.py` — pseudocode placeholder for tracking logic.
- `app/services/scheduler.py` — pseudocode placeholder for scheduling.
- `api/routes.py` — pseudocode for the API surface.
- `.env.example` — env template.
- `requirements.txt` — snippet of dependencies.