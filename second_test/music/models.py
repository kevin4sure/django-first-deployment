from django.db import models
from django.urls import reverse

# Create your models here.
# run 'python manage.py migrate' to automatically create database tables using migrations.
# run 'python manage.py makemigrations <app_name>' for any attribute changes happened in Models.
# after that, run 'python manage.py migrate' this will save the changes made in model attributes to the database.



class Album(models.Model):

    artist=models.CharField(max_length=250)
    album_title=models.CharField(max_length=500)
    genre=models.CharField(max_length=100)
    album_logo=models.ImageField(upload_to='album_images',blank=True)

    def get_absolute_url(self):
        return reverse('music_detail',kwargs={'pk':self.pk})
    def __str__(self):
        return self.album_title + '- '+ self.artist


class Song(models.Model):
    album=models.ForeignKey(Album,on_delete=models.CASCADE)    
    file_type= models.CharField(max_length=10)
    song_title=models.CharField(max_length=250)
    track_number=models.IntegerField(default=0)
    is_favourite=models.BooleanField(default=False)    

    def __str__(self):
        return self.song_title

#---open python shell from manage.py and create a class object with data.
#python manage.py shell
#>>> from music.models import Album,Song
#>>> al1=Album.objects.get(pk=1)
#>>> song1=Song()
#>>> song1.album=al1
# >>> song1.file_type='mp3'
# >>> song1.song_title='State of Grace'
# >>> song1.save()   <-- this statement will save the object to the database automatically

#---another simpler way is to use the admin section. 'localhost/admin' 