import requests

BASE_URL = "https://jsonplaceholder.typicode.com"  # asegúrate que esto esté definido

def test_create_user():
    payload = {
        "name": "Susan",
        "job": "QA Engineer"
    }

    response = requests.post(f"{BASE_URL}/users", json=payload)

    assert response.status_code == 201

    data = response.json()
    assert data["name"] == "Susan"