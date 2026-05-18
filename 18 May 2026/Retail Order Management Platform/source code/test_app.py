from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200

def test_order_status():
    client = app.test_client()
    response = client.get("/order-status")
    assert response.status_code == 200

def test_inventory():
    client = app.test_client()
    response = client.get("/inventory")
    assert response.status_code == 200
