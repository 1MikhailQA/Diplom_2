import allure
from endpoints import UserCRU

@allure.feature("Авторизация пользователя")
class TestUserLogin:

    @allure.title("Успешная авторизация")
    def test_login_user_success(self, create_user):
        _, payload, _, _ = create_user
        response = UserCRU.login_user(payload)
        assert response.status_code == 200
        assert response.json().get("success") == True
        assert "accessToken" in response.json()
        assert "refreshToken" in response.json()

    @allure.title("Авторизация с неверными данными")
    def test_login_user_invalid_credentials(self, user_data):
        invalid_payload = user_data.copy()
        invalid_payload["password"] = "wrong_password"

        response = UserCRU.login_user(invalid_payload)
        assert response.status_code == 401
        assert response.json() == {
            "success": False,
            "message": "email or password are incorrect"
        }