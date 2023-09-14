from django.test import TestCase

from my_testing.models import Person


class PersonTestCase(TestCase):
    def setUp(self):
        self.person1 = Person.objects.create(
            first_name="John", last_name="Doe", age=30
        )
        self.person2 = Person.objects.create(
            first_name="Edmond", last_name="Makolle", age=24
        )

    def test_present_himself(self):
        self.assertEqual(self.person1.present_himself(), "Hi, my name is John Doe")
        self.assertEqual(
            self.person2.present_himself(), "Hi, my name is Edmond Makolle"
        )

    def test_give_him_age(self):
        self.assertEqual(self.person1.give_him_age(), "I am 30 years old")
        self.assertEqual(self.person2.give_him_age(), "I am 24 years old")

    # def test_error(self):
    #     self.assertEqual(self.person.give_him_age(), "I am 31 years old")
