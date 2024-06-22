from faker import Faker


class TestData:
    def __init__(self):
        fake = Faker("pl_PL")
        self.user_name = fake.user_name()
        self.password = fake.password()

class CorrectUser:
    correct_username = "standard_user"
    correct_password = "secret_sauce"
