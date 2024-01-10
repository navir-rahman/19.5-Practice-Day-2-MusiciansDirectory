from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from musician.models import MusicianModel
# Create your models here.

class AlbumModel(models.Model):
    AlbumName = models.CharField(max_length=20)
    musician = models.ForeignKey(MusicianModel, on_delete=models.CASCADE)   # One-to-Many Relationships with musician model
    releaseDate = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])# Rating between 1-5
 

 