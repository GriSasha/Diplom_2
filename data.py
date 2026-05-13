class UrlApi:
    url = 'https://stellarburgers.education-services.ru/api/'

    create_user_api = f'{url}auth/register'
    login_api = f'{url}auth/login'
    order_api = f'{url}orders'
    delete_api = f'{url}auth/user'
    

class Response:
    order_without_ingredients = {"success": False, 
        "message": "Ingredient ids must be provided" }
    create_user_user_already_exist = {"success": False,
        "message": "User already exists"}
    create_user_missing_required_fields = {"success": False,
        "message": "Email, password and name are required fields"}
    login_incorrect_data = {"success": False,
        "message": "email or password are incorrect"}


