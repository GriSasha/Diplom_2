import requests
import allure

from data import UrlApi



# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
@allure.step('Отправляем post-запрос на регистрацию курьера со случайными логином, паролем и firstName ' \
'и сохраняем ответ в переменную response')
def register_new_user_and_return_email_password_name(user_payload):

    response = create_user(user_payload)

    if response.status_code == 201:
        return user_payload

    return None


@allure.step('Отправляем post-запрос на создание курьера')
def create_user(payload):
    return requests.post(UrlApi.create_user_api, json=payload)

@allure.step('Отправляем post-запрос на вход в учетную запись курьера')
def login_user(payload):
    return requests.post(UrlApi.login_api, json=payload)

@allure.step('Отправляем delete-запрос, чтобы удалить курьера из базы данных')
def delete_user_by_token(token):
    return requests.delete(UrlApi.delete_api, headers={'Authorization': token})


def delete_user_by_email_and_password(email, password):
    payload = {
        'email': email,
        'password': password
    }

    response = login_user(payload)

    if response.status_code == 200:
        token = response.json()['accessToken']
        delete_user_by_token(token)