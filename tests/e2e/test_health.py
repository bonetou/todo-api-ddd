def test_health(test_client):
    response = test_client.get("/_health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
