class Cat:

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def get_name(self) -> str:
        return self.name

    def get_gender(self) -> str:
        return self.gender

    def get_age(self) -> int:
        return self.age
