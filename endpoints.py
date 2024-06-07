from data import Urls
import requests
import allure

class UserCRU:
    @staticmethod
    @allure.step("Создание нового пользователя")
    def create_user(payload):
        response = requests.post(Urls.CREATE_USER_POST, json=payload)
        return response

    @staticmethod
    @allure.step("Авторизация пользователя")
    def login_user(payload):
        response = requests.post(Urls.LOGIN_USER_POST, json=payload)
        return response


    @staticmethod
    @allure.step("Удаление пользователя")
    def delete_user(token):
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.delete(Urls.DELETE_USER, headers=headers)
        return response

class Update:
    @staticmethod
    @allure.step("Обновление данных пользователя")
    def update_user(token, payload):
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.patch(Urls.DATA_UPDATE_USER_PATCH, headers=headers, json=payload)
        return response

    @staticmethod
    @allure.step("Обновление данных пользователя без авторизации")
    def update_user_without_auth(payload):
        response = requests.patch(Urls.DATA_UPDATE_USER_PATCH, json=payload)
        return response

class Order:
    @staticmethod
    @allure.step("Получение заказов пользователя с авторизацией")
    def get_user_orders(token):
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(Urls.ORDERS_USER_GET, headers=headers)
        return response

    @staticmethod
    @allure.step("Получение заказов пользователя без авторизации")
    def get_user_orders_without_auth():
        response = requests.get(Urls.ORDERS_USER_GET)
        return response

    @staticmethod
    @allure.step("Создание заказа с авторизацией")
    def create_order_with_auth(token, payload):
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.post(Urls.CREATE_ORDER_POST, headers=headers, json=payload)
        return response

    @staticmethod
    @allure.step("Создание заказа без авторизации")
    def create_order_without_auth(payload):
        response = requests.post(Urls.CREATE_ORDER_POST, json=payload)
        return response



