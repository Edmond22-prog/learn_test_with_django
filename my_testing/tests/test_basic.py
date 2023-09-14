from django.test import TestCase


class BasicTest(TestCase):
    
    def setUp(self):
        self.value1 = 2023
        self.value2 = 1999
    
    def test_value_1(self):
        self.assertEqual(self.value1, 2023)
    
    def test_value_2(self):
        self.assertEquals(self.value2, 1999)
    
    # def test_error(self):
    #     self.assertEquals(self.value1, self.value2)
