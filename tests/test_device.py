from fastapi.testclient import TestClient
# from ..server import app
'''
Testing API
References: https://fastapi.tiangolo.com/tutorial/testing/
'''
client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200