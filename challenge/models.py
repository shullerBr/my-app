from django.db import models
from django.utils import timezone
#from django.contrb.auth.models import User


class Challenge(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    #slug = models.SlugField()
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(default = 'default.jpg', blank=True)
    points_events = models.IntegerField(default=2)
    total_events = models.IntegerField()
    goal = models.IntegerField(default=40)
    beat_events = models.IntegerField(default=0)
    beat_points = models.IntegerField()
    porcent = models.IntegerField()

    #published_date = models.DateTimeField(blank=True, null=True)

    #def publish(self):
    #    self.published_date = timezone.now()
    #    self.save()

    def __str__(self):
        return self.title   
