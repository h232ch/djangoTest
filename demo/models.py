from datetime import datetime

from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=36, null=False, unique=True)
    description = models.TextField(max_length=256, blank=True)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=100)
    published = models.DateField()
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='covers/', blank=True)

    # it would express title on admin site
    def __str__(self):
        return self.title


class Comment:
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()


class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)


class Track(models.Model):
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    class Meta:
        unique_together = ['album', 'order']
        ordering = ['order']

    # String field relationship
    def __str__(self):
        return '%d: %s' % (self.order, self.title)