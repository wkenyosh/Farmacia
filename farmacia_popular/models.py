from django.db import models
from uuid import uuid4

# Create your models here.

class Farmacia_popular(models.Model):
    id_client= models.UUIDField(primary_key=True,default=uuid4,editable=False)
    Numero_COO = models.IntegerField()
    Data_Vendas = models.CharField(max_length=255)
    CPF = models.IntegerField()
    Auto_MS = models.IntegerField()

