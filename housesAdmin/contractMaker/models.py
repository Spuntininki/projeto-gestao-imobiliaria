from django.db import models

# Create your models here.
class Owner(models.Model):
    name = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=6, default=None)


class Renter(models.Model):
    name = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=6, default=None)


class Contract(models.Model):
    biding_owner = models.ForeignKey(Owner, on_delete=models.DO_NOTHING)
    biding_renter = models.ForeignKey(Renter, on_delete=models.DO_NOTHING)
    initial_date = models.DateField()
    end_date = models.DateField()
    rent_due_date = models.DateField()
    rent_amount = models.FloatField()
    deposit_amount = models.IntegerField()

class immobile(models.Model):
    biding_owner = models.ForeignKey(Owner, on_delete=models.DO_NOTHING)
    address = models.CharField(max_length=200)
    address_number = models.IntegerField()
    complement = models.CharField(max_length=60)
    district = models.CharField(max_length=120)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=2)
    cep = models.CharField(max_length=8)
    biding_contract = models.ForeignKey(Contract, on_delete=models.CASCADE)



    

