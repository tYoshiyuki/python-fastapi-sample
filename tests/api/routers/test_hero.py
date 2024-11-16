""" Heroエンドポイントのテスト """


def test_hero_ok(client):
    """hero 正常系
    hero が 正常に動作することを確認します。
    """

    # Arrange・Act
    response = client.get("/hero")

    # Assert
    assert response.status_code == 200
    assert response.json() == [
        {"id": 101, "age": 11, "name": "One", "secret_name": "one"},
        {"id": 102, "age": 22, "name": "Two", "secret_name": "two"},
        {"id": 103, "age": 33, "name": "Three", "secret_name": "three"},
    ]
