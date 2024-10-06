import pytest
from starlette.testclient import TestClient

from app.api.main import app

@pytest.fixture
def client():
    return TestClient(app)
