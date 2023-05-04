from faker import Faker


class DataGenerator:
    def __init__(self):
        self.fake = Faker()

    def first_name(self):
        first_name = self.fake.first_name()
        return first_name

    def last_name(self):
        last_name = self.fake.last_name()
        return last_name

    def zip_code(self):
        zip_code = self.fake.zipcode()
        return zip_code

