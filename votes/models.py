from django.db import models
from category.models import Category
from candidates.models import Candidate
# Create your models here.

class Women_Chair(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    party = models.CharField(max_length=200)
    votes = models.IntegerField(default='0')

    def __str__(self):
        return self.category.name
    

class Co_Chair(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    party = models.CharField(max_length=200)
    votes = models.IntegerField(default='0')

    def __str__(self):
        return self.category.name
    

class Youth_Chair(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    party = models.CharField(max_length=200)
    votes = models.IntegerField(default='0')

    def __str__(self):
        return self.category.name
    

class General_Chairman(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    party = models.CharField(max_length=200)
    votes = models.IntegerField(default='0')

    def __str__(self):
        return self.category.name
    

class Secretery_General(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    party = models.CharField(max_length=200)
    votes = models.IntegerField(default='0')

    def __str__(self):
        return self.category.name
    

class Financial_Secretery(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    party = models.CharField(max_length=200)
    votes = models.IntegerField(default='0')

    def __str__(self):
        return self.category.name