from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()

    def present_himself(self):
        return f"Hi, my name is {self.first_name} {self.last_name}"
    
    def give_him_age(self):
        return f"I am {self.age} years old"
