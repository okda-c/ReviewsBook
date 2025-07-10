from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class Review(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    review = models.TextField()