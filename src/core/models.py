from django.db import models
from django.db.models.base import Model

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) :
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) :
        return self.name

class Journal(models.Model):
    title = models.CharField(max_length=20)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    publish_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    reviewed = models.BooleanField(default=False)

    def __str__(self) :
        return self.title
