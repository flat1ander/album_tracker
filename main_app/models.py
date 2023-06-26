from django.db import models

class Album(models.Model):
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=250)
    image = models.CharField(max_length=500, default='default.jpg')
    info = models.TextField(max_length=20000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']