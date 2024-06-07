from endpoints import Update
from helper import UserRandom
import allure

class TestUpdateUser:
    @allure.title("Проверка успешного обновления данных пользователя")
    @allure.description("Проверка 200 кода и ответа 'success' == True")
    def test_update_user(self, update_user):
        token, new_user_data = update_user
        user = Update()
        response = user.update_user(token, new_user_data)
        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title("Проверка обновления для неавторизованного пользователя")
    @allure.description("Проверка 401 кода и ответа 'message' == 'You should be authorised'")
    def test_update_user_without_auth(self, user_data):
        new_user_data = {
            "email": UserRandom.generate_random_string(10) + "@yandex.ru",
            "name": UserRandom.generate_random_string(10)
        }
        user = Update()
        response = user.update_user_without_auth(new_user_data)
        assert response.status_code == 401 and response.json()['message'] == 'You should be authorised'