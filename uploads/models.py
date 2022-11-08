import email
from email.mime import image
from pydoc import describe
from statistics import mode
from django.db import models

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=90)
    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering=['-title']
        verbose_name_plural = 'Catrgories'



class Profile(models.Model):
    tech_stack = models.ForeignKey(Category, on_delete=models.CASCADE, unique=False)
    name = models.CharField(max_length=100, help_text='Enter your name')
    email = models.EmailField()
    image= models.FileField(upload_to = 'Files/')

    def __str__(self) -> str:
        return self.name
        
    def __repr__(self) -> str:
        return f' profile {self.name}, {self.image}'


class Book(models.Model):
    title = models.CharField(max_length=120)
    image = models.FileField(upload_to="files/")
    description = models.TextField(default="")
    price = models.IntegerField()
    discount = models.IntegerField()
    isbn = models.CharField(max_length=120, unique=True)
    is_published = models.BooleanField(default=True)
    rating = models.IntegerField()

    def __str__(self):
        return self.title




class UserInfoModels(models.Model):
    first_name = models.CharField(max_length=140)
    Last_name = models.CharField(max_length=140)
    email = models.EmailField()
    image = models.ImageField(upload_to='forms')

    def __str__(self) :
        return f'{self.first_name}'