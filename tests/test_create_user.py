import allure
import pytest
from endpoints import UserCRU

@allure.feature("Создание пользователя")
class TestCreateUser:

    @allure.title("Создание уникального пользователя")
    def test_create_user_success(self, user_data):
        response = UserCRU.create_user(user_data)
        assert response.status_code == 200


    @allure.title("Создание пользователя, который уже зарегистрирован")
    def test_create_user_already_exists(self, create_user):
        response, payload, login_response, token = create_user

        response_second = UserCRU.create_user(payload)
        assert response_second.status_code == 403
        assert response_second.json() == {
            "success": False,
            "message": "User already exists"
        }

    @allure.title("Создание пользователя без обязательного поля")
    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_create_user_missing_field(self, missing_field, user_data):

        user_data.pop(missing_field)

        response = UserCRU.create_user(user_data)
        assert response.status_code == 403
        assert response.json() == {
            "success": False,
            "message": "Email, password and name are required fields"
        }