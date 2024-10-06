def test_health_check_ok(client):
    """hello 正常系
    hello が 正常に動作することを確認します。
    """

    # Arrange・Act
    response = client.get("/hello")

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_say_hello_ok(client):
    """say_hello 正常系
    say_hello が 正常に動作することを確認します。
    """

    # Arrange・Act
    response = client.get("/hello/sample")

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": "Hello sample"}
