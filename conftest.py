import pytest

from base_methods import (
    register_new_user_and_return_email_password_name,
    delete_user_by_email_and_password)
    
from helpers import generate_user_payload



@pytest.fixture
def user_payload():
    return generate_user_payload()


@pytest.fixture
def registered_user(user_payload):
    user_data = register_new_user_and_return_email_password_name(user_payload)

    yield user_data

    if user_data is not None:
        delete_user_by_email_and_password(
            user_data['email'],
            user_data['password']
        )
        

        