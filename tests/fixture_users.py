import pytest


@pytest.fixture
def user():
    return {"id": 1, "nom": "Dupont", "email": "dupont@example.com"}
