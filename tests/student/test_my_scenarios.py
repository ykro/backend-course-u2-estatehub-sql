"""Tus tests propios.

Un buen test propio pasa con tu código y falla si siembras a propósito un error plausible
que los tests de la plantilla no atrapan: por ejemplo, un traslape con <= o una visita
buscada sin su propiedad. Compruébalo: mete el error, corre `uv run pytest tests/student -v`,
confirma que tu test falla y deshaz el cambio con `git restore`. Reescribir un test de la
plantilla no atrapa nada nuevo.

Reglas:
- Usa los fixtures de tests/conftest.py (client, engine, make_agency, make_property, book_visit).
- No crees conftest.py en esta carpeta.
- Cada test debe describir un escenario distinto a los tests de la plantilla, con datos propios
  y aserciones concretas sobre códigos HTTP y cuerpos JSON.
"""

from __future__ import annotations

import pytest
from fastapi.testclient import TestClient


def test_student_scenario_1(client: TestClient) -> None:
    """Escribe aquí un escenario del reto (por ejemplo, un borde de la ventana o del traslape)."""
    pytest.fail("Pendiente: escribe tu primer test propio")


def test_student_scenario_2(client: TestClient) -> None:
    """Escribe aquí un segundo escenario, distinto del primero."""
    pytest.fail("Pendiente: escribe tu segundo test propio")
