import allure
import pytest

from base_methods import login_user
from data import Response


class TestLogin:

    @allure.title('Существующий пользователь может авторизоваться')
    @allure.description('Вводим логин и пароль зарегистрированного пользователя, отправляем запрос на авторизацию,' \
    'ожидаем статус ответа - 200')
    def test_login_existing_user(self, registered_user):
        login_payload = {
            'email': registered_user['email'],
            'password': registered_user['password']
        }

        response = login_user(login_payload)

        assert response.status_code == 200

    @allure.title('Система вернет ошибку авторизации при вводе ошибочного email')
    @allure.description('Вводим ошибочный email и корректный пароль зарегистрированного пользователя, ' \
    'отправляем запрос на авторизацию,' \
    'ожидаем статус ответа - 401 и ответ: "success": False, ' \
    '"message": "email or password are incorrect"')
    def test_login_with_wrong_email_returns_error(self, registered_user):
        login_payload = {
            'email': 'wrong_email',
            'password': registered_user['password']
        }

        response = login_user(login_payload)

        assert response.status_code == 401
        assert response.json() == Response.login_incorrect_data


    @allure.title('Система вернет ошибку авторизации при вводе ошибочного пароля')
    @allure.description('Вводим зарегистрированный email и ошибочный пароль, ' \
    'отправляем запрос на авторизацию,' \
    'ожидаем статус ответа - 401 и ответ: "success": False, ' \
    '"message": "email or password are incorrect"')
    def test_login_with_wrong_password_returns_error(self, registered_user):
        login_payload = {
            'email': registered_user['email'],
            'password': 'wrong_password'
        }

        response = login_user(login_payload)

        assert response.status_code == 401
        assert response.json() == Response.login_incorrect_data