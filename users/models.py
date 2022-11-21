from django.contrib.auth.models import AbstractUser
from django.db import models
import random


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=13)

    def __str__(self):
        return self.username

class Code(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    number = models.CharField(max_length=6, null=True, blank=True)

    @property
    def genarate_code(self):
        number_list = list(range(10))
        code_items = ''
        for i in range(6):
            num = random.choice(number_list)
            code_items += str(num)
        self.number = code_items
        self.save()

    def __str__(self):
        return self.number