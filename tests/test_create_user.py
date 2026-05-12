import allure
import pytest

from base_methods import create_user, delete_user_by_token
from data import Response


class TestCreateUser:

    @allure.title('Курьера можно создать')
    @allure.description('Отправляем запрос на создание курьера, ожидаем статус ответа 201' \
    ' и сообщение об успешном создании')
    def test_create_user_success(self, user_payload):
        response = create_user(user_payload)

        assert response.status_code == 200
        token = response.json()['accessToken']

        delete_user_by_token(token)

    @allure.title('Нельзя создать двух одинаковых курьеров')
    @allure.description('Создаем курьера, ожидаем статус ответа 201, ' \
    'далее пытаемся создать курьера с теми же данными, ожидаем статус ответа 409')
    def test_create_two_same_users_returns_error(self, user_payload):
        first_response = create_user(user_payload)
        second_response = create_user(user_payload)

        assert first_response.status_code == 200
        assert second_response.json() == Response.create_user_user_already_exist

        token = first_response.json()['accessToken']
        delete_user_by_token(token)

    @allure.title('Для создания курьера нужно передать login')
    @allure.description('Не заполняем login при заполнении данных для создания учетной записи курьера, ' \
    'отправляем запрос, ожидаем статус ответа 400 и сообщения об ошибке')
    def test_create_user_without_email_returns_error(self, user_payload):
        user_payload.pop('email')

        response = create_user(user_payload)

        assert response.status_code == 403
        assert response.json() == Response.create_user_missing_required_fields

    @allure.title('Для создания курьера нужно передать password')
    @allure.description('Не заполняем password при заполнении данных для создания учетной записи курьера, ' \
    'отправляем запрос, ожидаем статус ответа 400 и сообщения об ошибке')
    def test_create_user_without_password_returns_error(self, user_payload):
        user_payload.pop('password')

        response = create_user(user_payload)

        assert response.status_code == 403
        assert response.json() == Response.create_user_missing_required_fields

    @allure.title('Для создания курьера нужно передать password')
    @allure.description('Не заполняем password при заполнении данных для создания учетной записи курьера, ' \
    'отправляем запрос, ожидаем статус ответа 400 и сообщения об ошибке')
    def test_create_user_without_name_returns_error(self, user_payload):
        user_payload.pop('name')

        response = create_user(user_payload)

        assert response.status_code == 403
        assert response.json() == Response.create_user_missing_required_fields

   