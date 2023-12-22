from unicodedata import name
from django.db import models

# Create your models here.
# class Person(models.Model):
#     first_name = models.CharField(max_length=20)
#     email = models.EmailField()
#     phone = models.CharField(max_length=20)
#
#     def __str__(self):
#         return f"{self.last_name}, {self.first_name}"

#
# class Customer(models.Model):
#     name = models.CharField(max_length=255)
#
#
# class Vehicle(models.Model):
#     name = models.CharField(max_length=255)
#     customer = models.ForeignKey(
#         Customer,
#         on_delete=models.CASCADE,
#         related_name='Vehicle'
#     )


class Logger(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    time_log = models.TimeField(help_text="Enter the exact time!")

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    # first_name = models.TextField()

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class Menu(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()

    def __str__(self):
        return self.name

