def test_health_check_ok(client):
    """health_check 正常系
    health_check が 正常に動作することを確認します。
    """

    # Arrange・Act
    response = client.get("/")

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": "success."}

