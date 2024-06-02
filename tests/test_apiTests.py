import requests


class TestAPI:
    def test_get_items(self):
        response = requests.get('http://localhost:3000/api/v1/items')
        assert response.status_code == 200

    def test_log_in(self):
        response = requests.post('http://localhost:3000/api/v1/login', {"username": "test1", "password": "12345678"})
        response_json = response.json()
        assert response.status_code == 200
        response = requests.get('http://localhost:3000/api/v1/user', headers={"Authorization": "Bearer " + response_json['token']})
        response_json = response.json()
        assert response.status_code == 200

    def test_user_not_logged_in(self):
        response = requests.get('http://localhost:3000/api/v1/user',headers={"Authorization": "Bearer test"})
        assert response.status_code == 403
