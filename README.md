# EstateHub SQL API

API de gestión inmobiliaria con persistencia relacional en SQLModel, filtros paginados y agenda de visitas sin colisiones.

## Unidad 2

Plantilla de la Unidad 2 del curso.

## Requisitos

- [uv](https://docs.astral.sh/uv/), que instala Python 3.13 y las dependencias exactas de `uv.lock`.

## Instalar y correr

```bash
uv sync
SEED_DEMO_DATA=true uv run uvicorn app.main:app --reload --port 8000   # con datos de demo

```

La consola queda en http://127.0.0.1:8000 y Swagger en `/docs`.
Sin `SEED_DEMO_DATA=true` la base empieza vacía.

## Tests

```bash
uv run pytest -v                  # solo los tests
uv run ruff check . && uv run ruff format --check . && uv run pytest -v   # chequeo completo
```

El archivo `AGENTS.md` trae las reglas para el asistente de IA.

El enunciado del reto, la rúbrica y la guía paso a paso están en el curso.
