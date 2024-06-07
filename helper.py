import random
import string
from faker import Faker


class UserRandom:
    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase + string.digits
        return ''.join(random.choice(letters) for _ in range(length))

    @staticmethod
    def generate_random_user_data():
        faker = Faker()
        email = faker.email()
        password = UserRandom.generate_random_string(10)
        name = faker.name()
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        return payload