from django.db import models
# Create your models here.
class Slider(models.Model):
    photo=models.URLField( max_length=10000)

    def __str__(self):
        return 'success'

class Advertisement(models.Model):
    photo=models.URLField( max_length=10000)

    def __str__(self):
        return 'success'


class Advertisement2(models.Model):
    photo=models.URLField( max_length=10000)

    def __str__(self):
        return 'success'

class Flavours(models.Model):
    Flavour_title=models.CharField(max_length=128)
    Description=models.CharField(max_length=512)
    cake_photo=models.URLField( max_length=10000)

    def __str__(self):
        return self.Flavour_title

class FlavouredCake(models.Model):
    flavour=models.ForeignKey("Flavours",  on_delete=models.CASCADE)
    title=models.CharField(max_length=128)
    Description=models.CharField(max_length=155)
    cake_photo=models.URLField( max_length=10000)
    price=models.CharField(max_length=50)
    cut_price=models.CharField(max_length=50)
    def __str__(self):
        return self.title

class PhotoCakes(models.Model):
    Cake_title=models.CharField(max_length=128)
    Description=models.CharField(max_length=512)
    cake_photo=models.URLField( max_length=10000)

    def __str__(self):
        return self.Cake_title

class DesignerCakes(models.Model):
    Cake_title=models.CharField(max_length=128)
    Description=models.CharField(max_length=512)
    cake_photo=models.URLField( max_length=10000)

    def __str__(self):
        return self.Cake_title

class PremiumTable(models.Model):
    cake_title=models.CharField(max_length=128)
    Description=models.CharField(max_length=512)
    cake_photo=models.URLField( max_length=10000)

    def __str__(self):
        return self.cake_title

class SomethingElse(models.Model):
    title=models.CharField(max_length=128)
    photo=models.URLField( max_length=10000)

    def __str__(self):
        return self.title

class CustomizeOrderTable(models.Model):
    Name=models.CharField(max_length=128)
    Phone=models.CharField( max_length=128)
    Details=models.CharField(max_length=1024,null=True)
    Email=models.EmailField( max_length=254,null=True)
    
    
    

    def __str__(self):
        return self.Name

class DryCakes_and_Cookie(models.Model):
    title=models.CharField(max_length=128)
    Description=models.CharField(max_length=512)
    cake_photo=models.URLField( max_length=10000)

    def __str__(self):
        return self.title

class BrowseBlog(models.Model):
    title=models.CharField(max_length=128)
    photo=models.URLField( max_length=10000)
    def __str__(self):
        return self.title

class shakes_and_Smoothie(models.Model):
    title=models.CharField(max_length=128)
    Description=models.CharField(max_length=512)
    cake_photo=models.URLField( max_length=10000)
    def __str__(self):
        return self.title

class CupCakes_and_Brownie(models.Model):
    title=models.CharField(max_length=128)
    Description=models.CharField(max_length=512)
    cake_photo=models.URLField( max_length=10000)
    def __str__(self):
        return self.title
