import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_single_user():
    response = requests.get(f"{BASE_URL}/users/2")

    assert response.status_code == 200

    data = response.json()
    assert data["id"] == 2