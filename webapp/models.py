from django.db import models

# Create your models here.

class Beer(models.Model):
    name = models.CharField(max_length=60, blank=False, null=False)
    price = models.FloatField()
    creation = models.DateField()

    def __str__(self):
        return f'id: {self.id}, name: {self.name}, price: {self.price}, creation: {self.creation}'
