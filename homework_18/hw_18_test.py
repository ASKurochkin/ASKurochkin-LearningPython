"""Testing class Person from homework 17 (teacher version)"""
import unittest
from homework.homework_18.hw_18_class_for_test import Person, PersonVerify, PersonData


class TestPerson(unittest.TestCase):
    def setUp(self) -> None:
        self.person = Person
        self.verify = PersonVerify
        self.data = PersonData

    def tearDown(self) -> None:
        del self.person
        del self.verify
        del self.data

    def test_verify_full_name(self):
        self.assertRaises(TypeError, self.verify.verify_full_name, 10)
        self.assertRaises(TypeError, self.verify.verify_full_name, ' ')
        self.assertRaises(TypeError, self.verify.verify_full_name, 'Иванов Иван')
        self.assertRaises(TypeError, self.verify.verify_full_name, '1 2 3')
        self.assertEqual(self.verify.verify_full_name('Иванов Иван Иванович'), None)

    def test_verify_age(self):
        self.assertRaises(TypeError, self.verify.verify_age, 'Восемнадцать')
        self.assertRaises(ValueError, self.verify.verify_age, 130)
        self.assertEqual(self.verify.verify_age(18), None)

    def test_verify_weight(self):
        self.assertRaises(TypeError, self.verify.verify_weight, 50)
        self.assertRaises(ValueError, self.verify.verify_weight, 160.1)
        self.assertEqual(self.verify.verify_weight(50.7), None)

    def test_verify_id_card(self):
        self.assertRaises(TypeError, self.verify.verify_id_card, 50)
        self.assertRaises(ValueError, self.verify.verify_id_card, 'ВР 415141')
        self.assertEqual(self.verify.verify_id_card('ВР-415141'), None)

    def test_verify_all(self):
        self.assertEqual(self.verify.verify_all(self.data('Иванов Иван Иванович', 36, 'ВР-415141', 101.3)), None)

    def test_full_name(self):
        self.person.full_name = 'Иванов Иван Иванович'
        name = self.person.full_name
        self.assertEqual(name, 'Иванов Иван Иванович')

    def test_age(self):
        self.person.age = 20
        age = self.person.age
        self.assertEqual(age, 20)

    def test_weight(self):
        self.person.weight = 81.1
        weight = self.person.weight
        self.assertEqual(weight, 81.1)

    def test_id_card(self):
        self.person.id_card = 'ВР-415141'
        id = self.person.id_card
        self.assertEqual(id, 'ВР-415141')


if __name__ == '__main__':
    unittest.main()
