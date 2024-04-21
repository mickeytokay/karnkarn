from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=255, unique=True)


    def get_url(self):
        return reverse('votes_by_category', args=[self.slug])

    def __str__(self):
        return self.name
    