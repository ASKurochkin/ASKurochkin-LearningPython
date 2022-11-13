"""Create user base class"""
import re


class Person:
    """Base class for creating a user"""
    MIN_AGE = 16
    MAX_AGE = 66
    MIN_WEIGHT = 40.0
    MAX_WEIGHT = 130.0

    def __init__(self):
        self.__name = 'Иванов Иван Иванович'
        self.__age = 33
        self.__ID = 'ВР-415141'
        self.__weight = 80.0

    def get_name(self):
        return f'Users name is: {self.__name}'

    def get_age(self):
        return f'Users age is: {self.__age}'

    def get__id(self):
        return f'Users ID is: {self.__ID}'

    def get_weight(self):
        return f'Users weigh is: {self.__weight}'

    def get_all_persons_data(self):
        return f"User's personal data is:\n" \
               f"Name: {self.__name}\n" \
               f"Age: {self.__age}\n" \
               f"ID: {self.__ID}\n" \
               f"Weigh: {self.__weight}\n"

    def set_name(self):
        name = input("Enter your full name (for example Иванов Иван Иванович): ")
        if self.__check_name(name):
            self.__name = name

    def set_age(self):
        age = input("Enter your age in full years (for example 33): ")
        if self.__check_age(age):
            self.__age = age

    def set_id(self):
        id = input("Enter your ID (for example НЮ-123456): ")
        if self.__check_id(id):
            self.__ID = id

    def set_weight(self):
        weight = input("Enter your weight in kg (for example 75.1): ")
        if self.__check_weight(weight):
            self.__weight = weight

    def __check_name(self, name):
        """Checking that the full name entered does not contain numbers and is written in Cyrillic"""
        if name == '':
            exit()
        elif re.search(r'[0123456789]', name):
            print("Name cannot contain numbers. Try again.")
            exit()
        elif not re.search(r' ', name):
            print("Full name must contain words with spaces. Try again.")
            exit()
        elif not re.search(r'[а-яА-ЯёЁ]', name):
            print("The name must be entered in Cyrillic characters. Try again.")
            exit()
        return name

    def __check_age(self, age):
        """Checking that age entered is digit, and it within the allowed age range"""
        if age == '':
            exit()
        elif not age.isdigit():
            print('Age must be represented as integer. Try again.')
            exit()
        elif not self.MIN_AGE <= int(age) <= self.MAX_AGE:
            print(f'Your age {age} years does not match the permitted age group'
                  f' from {self.MIN_AGE} to {self.MAX_AGE} years. Goodbye.')
            exit()
        return age

    def __check_id(self, id):
        """Checking that ID entered corresponds to the format of the Ukrainian passport"""
        if id == '':
            exit()
        elif not re.search(r'[А-ЯЁ]{2}-[0123456789]{6}', id):
            print(f'The ID you entered is not in the correct format.\n'
                  f'Compare with the example again. Your ID: {id}. Example: НЮ-123456')
            exit()
        return id

    def __check_weight(self, weight):
        """Checking that weight entered is digit, and it within the allowed weight range"""
        if weight == '':
            exit()
        elif not weight.isdigit():
            try:
                float(weight)
                return weight
            except ValueError:
                print(f'Your weight must be float. Compare with the example and try again')
                exit()
        elif not self.MIN_WEIGHT <= float(weight) <= self.MAX_WEIGHT:
            print(f'Your weight {weight} kg. does not match the permitted weight group'
                  f' from {self.MIN_WEIGHT} to {self.MAX_WEIGHT} kilograms. Goodbye.')
            exit()
        return weight


if __name__ == '__main__':
    user = Person()
    user.set_name()
    user.set_age()
    user.set_id()
    user.set_weight()
    print(user.get_all_persons_data())
