import allure
import pytest

from base_methods import login_user, create_order
from data import Response, Ingredients


class TestCreateOrder:

    @allure.title('Авторизированный пользователь может создать заказ')
    @allure.description('Вводим логин и пароль авторизированного пользователя, получаем его токен,'
    'отправляем запрос на создание заказа под авторизированной учетной записью. ' \
    'Ожидаем статус ответа 200')
    def test_create_order_with_autorisation(self, registered_user):
        login_payload = {
            'email': registered_user['email'],
            'password': registered_user['password']
        }

        auth_response = login_user(login_payload)

        token = auth_response.json()['accessToken']
        order_payload = Ingredients.exist_ingredients
        order_response = create_order(order_payload, token)

        assert order_response.status_code == 200


    @allure.title('Неавторизированный пользователь может создать заказ')
    @allure.description('Отправляем запрос на создание заказа, не авторизируясь. ' \
    'Ожидаем статус ответа 200')
    def test_create_order_without_autorisation(self):
    
        order_payload = Ingredients.exist_ingredients
        order_response = create_order(order_payload)

        assert order_response.status_code == 200


    @allure.title('Можно создать заказ, указав ингредиенты')
    @allure.description('Отправляем запрос на создание заказа с ингредиентами. ' \
    'Ожидаем статус ответа 200')
    def test_create_order_with_ingredients(self):

        order_payload = Ingredients.exist_ingredients
        order_response = create_order(order_payload)

        assert order_response.status_code == 200


    @allure.title('Нельзя создать заказ без ингредиентов')
    @allure.description('Отправляем запрос на создание заказа без ингредиентами. ' \
    'Ожидаем статус ответа 400 и ответ: "success": False, ' \
    '"message": "Ingredient ids must be provided"')
    def test_create_order_without_ingredients(self):

        order_payload = Ingredients.empty_ingredients
        order_response = create_order(order_payload)

        assert order_response.status_code == 400
        assert order_response.json() == Response.order_without_ingredients


    @allure.title('Нельзя создать заказ с неверным хешем ингредиентов')
    @allure.description('Отправляем запрос на создание заказа с неверным хешем ингредиентов. ' \
    'Ожидаем статус ответа 500')
    def test_create_order_with_wrong_hash(self):

        order_payload = Ingredients.wrong_ingredients
        order_response = create_order(order_payload)

        assert order_response.status_code == 500
      