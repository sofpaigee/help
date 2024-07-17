from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Incident(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    tags = models.ManyToManyField(Tag)
    date_reported = models.DateTimeField(default=timezone.now)
    files = models.FileField(upload_to='incident_pictures', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class IncidentFile(models.Model):
    incident = models.ForeignKey('Incident', related_name='files', on_delete=models.CASCADE)
    file = models.FileField(upload_to='incident_pictures')

    def __str__(self):
        return self.file.name