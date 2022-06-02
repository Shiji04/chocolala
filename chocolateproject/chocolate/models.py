from django.db import models

# Create your models here.

class Chocolate(models.Model):
    name=models.CharField(max_length=100)
    class Meta:
        db_table = 'Chocolate'
        ordering = ['name']
    def __str__(self):
        return self.name


class District(models.Model):
    name=models.CharField(max_length=100)
    class Meta:
        db_table = 'District'
        ordering = ['name']
    def __str__(self):
        return self.name
class Branch(models.Model):
    name=models.CharField(max_length=30)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    class Meta:
        db_table = 'Branch'
        ordering = ['name']


    def __str__(self):

        return self.name
class Order(models.Model):
    name=models.CharField(max_length=250)
    phone=models.IntegerField()
    email=models.EmailField()
    address=models.CharField(max_length=150)
    district=models.ForeignKey(District, on_delete=models.SET_NULL,blank=True,null=True)
    branch=models.ForeignKey(Branch, on_delete=models.SET_NULL,blank=True,null=True)
    chocolet=models.ForeignKey(Chocolate, on_delete=models.SET_NULL,blank=True,null=True)
    quantity=models.IntegerField()

    class Meta:
        db_table = 'Order'
        ordering = ['name']
    def __str__(self):
        return self.name



