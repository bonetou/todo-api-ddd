from fastapi.testclient import TestClient
import pytest


@pytest.fixture(scope="session")
def test_client():
    from main import app
    return TestClient(app)
