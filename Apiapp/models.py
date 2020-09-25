from django.db import models


class Employees(models.Model):
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    emp_id = models.IntegerField()

    def __str__(self):
        return self.firstname


class Authority(models.Model):
    Auth_name = models.CharField(max_length=10)
    Auth_id = models.IntegerField
    Auth_Section = models.CharField(max_length=20)

    def __str__(self):
        return self.Auth_name



class Buyer(models.Model):
    Buyer_id = models.IntegerField()
    Buyer_name = models.CharField(max_length=20)
    Buyer_Address = models.CharField(max_length=50)
    Iteam = models.CharField(max_length=50)
    Purchased_Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Buyer_name
