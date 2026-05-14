import requests
import allure

from data import UrlApi


@allure.step('Отправляем post-запрос на регистрацию пользователя со случайными email, паролем и именем ' \
'и сохраняем ответ в переменную response')
def register_new_user_and_return_email_password_name(user_payload):

    response = create_user(user_payload)

    if response.status_code == 200:
        return user_payload

    return None


@allure.step('Отправляем post-запрос на создание пользователя')
def create_user(payload):
    return requests.post(UrlApi.create_user_api, json=payload)

@allure.step('Отправляем post-запрос на вход в учетную запись пользователя')
def login_user(payload):
    return requests.post(UrlApi.login_api, json=payload)

@allure.step('Отправляем delete-запрос, чтобы удалить пользователя из базы данных по токену')
def delete_user_by_token(token):
    return requests.delete(UrlApi.delete_api, headers={'Authorization': token})


@allure.step('Отправляем delete-запрос, чтобы удалить пользователя из базы данных по email и паролю')
def delete_user_by_email_and_password(email, password):
    payload = {
        'email': email,
        'password': password
    }

    response = login_user(payload)

    if response.status_code == 200:
        token = response.json()['accessToken']
        delete_user_by_token(token)

@allure.step('Отправляем post-запрос на создание заказа')
def create_order(payload, token=None):
    headers = {}

    if token is not None:
        headers = {'Authorization': token}

    return requests.post(
        UrlApi.order_api,
        json=payload,
        headers=headers
    )