""" pytestの共通設定モジュール """
import pytest
from starlette.testclient import TestClient

from app.api.main import app
from app.db import create_db_and_tables, seed


@pytest.fixture
def client():
    """ テストクライアントを取得する """
    return TestClient(app)


@pytest.fixture(scope="session")
def init_db():
    """ DBの初期化を行う """
    # テーブル作成
    create_db_and_tables()

    # 初期データ投入
    seed()
