from django.db import models
from django.urls import reverse
# Create your models here.

class Block(models.Model):
    block = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)


    def get_url(self):
        return reverse('members_by_block', args=[self.slug])

    def __str__(self):
        return self.block
    