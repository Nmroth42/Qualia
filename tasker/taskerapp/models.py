from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    logo = models.ImageField(upload_to='task_logo/', blank=False)

    def __str__(self):
        return self.name

class Gig(models.Model): 
    CATEGORY_CHOICES = (
        ("GD", "Graphics and Design"),
        ("DM", "Digital and Marketing"),
        ("VA", "Video and Animation"),
        ("MA", "Music and Audio"),
        ("PT", "Programming and Tech")
    )
    title = models.CharField(max_length=500)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    description = models.CharField(max_length=2000)
    price = models.IntegerField(default=0)
    photo = models.FileField(upload_to='gigs')
    status = models.BooleanField(default=True)
    user = models.ForeignKey(User)
    create_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
# Create your models here.
