import pytest
from starlette.testclient import TestClient

from app.api.main import app
from app.db import create_db_and_tables, seed

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture(scope="session")
def init_db():
    # テーブル作成
    create_db_and_tables()

    # 初期データ投入
    seed()