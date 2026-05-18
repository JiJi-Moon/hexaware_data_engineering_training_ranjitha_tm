from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200

def test_appointment_status():
    client = app.test_client()
    response = client.get("/appointment-status")
    assert response.status_code == 200

def test_doctor_availability():
    client = app.test_client()
    response = client.get("/doctor-availability")
    assert response.status_code == 200
