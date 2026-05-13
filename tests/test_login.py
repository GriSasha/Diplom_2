import allure
import pytest

from base_methods import login_user
from data import Response


class TestLogin:

    def test_login_existing_user(self, registered_user):
        login_payload = {
            'email': registered_user['email'],
            'password': registered_user['password']
        }

        response = login_user(login_payload)

        assert response.status_code == 200

    def test_login_with_wrong_email_returns_error(self, registered_user):
        login_payload = {
            'email': 'wrong_email',
            'password': registered_user['password']
        }

        response = login_user(login_payload)

        assert response.status_code == 401
        assert response.json() == Response.login_incorrect_data

    def test_login_with_wrong_password_returns_error(self, registered_user):
        login_payload = {
            'email': registered_user['email'],
            'password': 'wrong_password'
        }

        response = login_user(login_payload)

        assert response.status_code == 401
        assert response.json() == Response.login_incorrect_data