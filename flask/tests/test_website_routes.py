import pytest
from src.app import app

@pytest.fixture(autouse=True)
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_main(client):
    response = client.get("/")
    assert response.status_code == 200
    
    assert b"Hello World!" in response.data
