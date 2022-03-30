from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_summ():
    response = client.get("/calc?expression=5%2b3")
    assert response.status_code == 200
    assert response.json()['result'] == '8'


def test_diff():
    response = client.get("/calc?expression=2-7")
    assert response.status_code == 200
    assert response.json()['result'] == '-5'


def test_mult():
    response = client.get("/calc?expression=4*3")
    assert response.status_code == 200
    assert response.json()['result'] == '12'


def test_dev():
    response = client.get("/calc?expression=7/2")
    assert response.status_code == 200
    assert response.json()['result'] == '3.5'
