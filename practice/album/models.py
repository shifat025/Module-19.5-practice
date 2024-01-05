from django.db import models
from django.contrib.auth.models import User

lists = (('1','1'),('2','2'),('3','3'),('4','4'),('5','5'))

# Create your models here.
class albums(models.Model):
    Album_name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    albums_release_date = models.DateField()
    album_rating = models.CharField(max_length = 5, choices=lists)
    Instrument_type = models.CharField(max_length=50)

    def __str__(self):
        return self.Album_name