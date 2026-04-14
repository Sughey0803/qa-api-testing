import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_users():
    response = requests.get(f"{BASE_URL}/users")

    # Validar status code
    assert response.status_code == 200

    # Validar JSON
    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0