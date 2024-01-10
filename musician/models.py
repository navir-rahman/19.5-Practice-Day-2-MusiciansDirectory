from django.db import models

# Create your models here.
class MusicianModel(models.Model):
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    Email    = models.EmailField()
    PhoneNumber = models.CharField(max_length=20)
    InstrumentType = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.FirstName} {self.LastName}"