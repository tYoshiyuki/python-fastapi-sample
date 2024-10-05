from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_root_ok():
    """root 正常系
    root が 正常に動作することを確認します。
    """

    # Arrange・Act
    response = client.get("/")

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

