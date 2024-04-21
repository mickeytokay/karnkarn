from django.db import models



# Create your models here.
class Candidate(models.Model):
    COMMUNITY_CHOICES = (
        ('Block A', 'Block A'),
        ('Block B', 'Block B'),
        ('Block C', 'Block C'),
        ('Block D', 'Block D'),
        ('Block E', 'Block E'),
        ('Block F', 'Block F'),  
    )    
    
    candidate = models.CharField(max_length=200)
    positions = models.CharField(max_length=200)
    party = models.CharField(max_length=200)
    block = models.CharField(max_length=50,choices=COMMUNITY_CHOICES,default='BLOCK A')
    nationality = models.CharField(max_length=200, default='Liberian')
    photo = models.ImageField(upload_to='photos/candidates', default='image.jpg' , blank=True)

    def __str__(self):
        return self.candidate
    
