import allure
from endpoints import Order


class TestOrders:
    @allure.title("Проверка успешного создания заказа с авторизацией")
    def test_create_order(self, create_user):
        order = Order()
        payload = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]}
        response = order.create_order_with_auth(create_user[3], payload)
        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title("Проверка создания заказа без авторизации")
    def test_create_order_without_auth(self, create_user):
        order = Order()
        payload = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]}
        response = order.create_order_without_auth(payload)
        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title("Проверка создания заказа без ингридиентов без авторизации")
    def test_create_order_no_ingridient_no_token(self):
        order = Order()
        payload = {"ingredients": []}
        response = order.create_order_without_auth(payload)
        assert response.status_code == 400 and response.json()['message'] == 'Ingredient ids must be provided'

    @allure.title("Проверка создания заказа без ингридиентов с авторизацией")
    def test_create_order_no_ingridient(self, create_user):
        order = Order()
        payload = {"ingredients": []}
        response = order.create_order_with_auth(create_user[3], payload)
        assert response.status_code == 400 and response.json()['message'] == 'Ingredient ids must be provided'

    @allure.title("Проверка создания заказа с неверным хешем ингредиентов")
    def test_create_order_invalid_hash(self):
        order = Order()
        payload = {"ingredients": ["61c0c5a7182001bfaaa6d", "61c0c5a71ddf82001bdaaa6f"]}
        response = order.create_order_without_auth(payload)
        assert response.status_code == 500 and 'Internal Server Error' in response.text