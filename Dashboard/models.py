from django.db import models

# Create your models here.
class Abc(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")
