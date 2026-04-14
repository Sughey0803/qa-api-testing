BASE_URL = "https://jsonplaceholder.typicode.com"
import requests
def test_user_not_found():
    response = requests.get(f"{BASE_URL}/users/999")

    assert response.status_code == 404