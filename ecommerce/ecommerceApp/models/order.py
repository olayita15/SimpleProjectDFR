# models.py
from django.db import models

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(auto_now_add=True)
    client = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id} - {self.client}"
