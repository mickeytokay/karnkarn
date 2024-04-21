from django.db import models
from block.models import Block

class Member(models.Model):
    full_name = models.CharField(max_length=200, unique=True)
    photo = models.ImageField(upload_to='photos/members', blank=True)
    date_of_birth = models.DateField()
    block = models.ForeignKey(Block, on_delete=models.CASCADE)
    nationality = models.CharField(max_length=200)
    occupation = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)


    def __str__(self):
        return self.full_name
    