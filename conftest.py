import pytest
import requests
from data import Urls
from helper import UserRandom
from endpoints import UserCRU

@pytest.fixture(scope='function')
def user_data():
    return UserRandom.generate_random_user_data()

@pytest.fixture(scope='function')
def create_user():
    payload = UserRandom.generate_random_user_data()
    response = UserCRU.create_user(payload)

    login_url = Urls.LOGIN_USER_POST
    login_response = requests.post(login_url, json=payload)
    token = login_response.json().get("accessToken")

    if token and token.startswith("Bearer "):
        token = token.split("Bearer ")[1]

    yield response, payload, login_response, token

    if token:
        requests.delete(Urls.DELETE_USER, headers={'Authorization': f'Bearer {token}'})

@pytest.fixture(scope='function')
def update_user(create_user):
    response, payload, login_response, token = create_user
    new_user_data = {
        "email": UserRandom.generate_random_string(10) + "@yandex.ru",
        "name": UserRandom.generate_random_string(10)
    }
    return token, new_user_data
