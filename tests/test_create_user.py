import allure
import pytest

from base_methods import create_user, delete_user_by_token
from data import Response


class TestCreateUser:

    @allure.title('Пользователя можно создать')
    @allure.description('Отправляем запрос на создание пользователя, ожидаем статус ответа 200')
    def test_create_user_success(self, user_payload):
        response = create_user(user_payload)

        assert response.status_code == 200
        token = response.json()['accessToken']

        delete_user_by_token(token)

    @allure.title('Нельзя создать двух одинаковых пользователей')
    @allure.description('Создаем пользователя, ожидаем статус ответа 200, ' \
    'далее пытаемся создать пользователя с теми же данными, ожидаем статус ответа 403' \
    'и ответ: "success": False, "message": "User already exists"')
    def test_create_two_same_users_returns_error(self, user_payload):
        first_response = create_user(user_payload)
        second_response = create_user(user_payload)

        assert first_response.status_code == 200
        assert second_response.status_code == 403
        assert second_response.json() == Response.create_user_user_already_exist

        token = first_response.json()['accessToken']
        delete_user_by_token(token)

    @allure.title('Для создания пользователя нужно передать email')
    @allure.description('Не заполняем email при заполнении данных для создания учетной записи пользователя, ' \
    'отправляем запрос, ожидаем статус ответа 403 и ответ:' \
    '"success": False,  "message": "Email, password and name are required fields"')
    def test_create_user_without_email_returns_error(self, user_payload):
        user_payload.pop('email')

        response = create_user(user_payload)

        assert response.status_code == 403
        assert response.json() == Response.create_user_missing_required_fields

    @allure.title('Для создания пользователя нужно передать password')
    @allure.description('Не заполняем password при заполнении данных для создания учетной записи пользователя, ' \
    'отправляем запрос, ожидаем статус ответа ожидаем статус ответа 403 и ответ:' \
    '"success": False,  "message": "Email, password and name are required fields"')
    def test_create_user_without_password_returns_error(self, user_payload):
        user_payload.pop('password')

        response = create_user(user_payload)

        assert response.status_code == 403
        assert response.json() == Response.create_user_missing_required_fields

    @allure.title('Для создания курьера нужно передать name')
    @allure.description('Не заполняем name при заполнении данных для создания учетной записи пользователя, ' \
    'отправляем запрос, ожидаем статус ответа 403 и ответ:' \
    '"success": False,  "message": "Email, password and name are required fields"')
    def test_create_user_without_name_returns_error(self, user_payload):
        user_payload.pop('name')

        response = create_user(user_payload)

        assert response.status_code == 403
        assert response.json() == Response.create_user_missing_required_fields

   