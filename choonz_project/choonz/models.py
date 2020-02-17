from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.
class Playlist(models.Model):
    max_length_char = 128
    name = models.CharField(max_length=max_length_char, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Playlist, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Playlists'

    def __str__(self):
        return self.name

class Page(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    title = models.CharField(max_length=Playlist.max_length_char)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    # link UserProfile to User model instance
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Addition attributes to include
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username


