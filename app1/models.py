from django.db import models

# Create your models here.
class employe(models.Model):
    name = models.CharField(max_length=50)
    id_no = models.IntegerField()
    email = models.EmailField()
    