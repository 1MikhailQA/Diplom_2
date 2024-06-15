import allure
from endpoints import Order


class TestUserOrders:
    @allure.title("Получение заказов авторизованным пользователем")
    def test_get_orders_authenticated(self, create_user):
        token = create_user[3]
        response = Order.get_user_orders(token)
        assert response.status_code == 200
        assert response.json().get('success') == True
        assert 'orders' in response.json()

    @allure.title("Получение заказов неавторизованным пользователем")
    def test_get_orders_unauthenticated(self):
        response = Order.get_user_orders_without_auth()
        assert response.status_code == 401
        assert response.json().get('success') == False
        assert response.json().get('message') == "You should be authorised"