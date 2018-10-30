from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField

class Profile(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE, )
    status = models.CharField(max_length=500)
    logo = models.ImageField(upload_to='task_logo/', blank=False)
    
   # def __str__(self):
    #    return self.name

class Gig(models.Model): 
    CATEGORY_CHOICES = (
        ("ЕГЭ егэ английский Английский Язык язык", "ЕГЭ:Английский язык"),
        ("IELTS ielts шудеы", "IELTS"),
        ("TOEFL toefl ещуад", "TOEFL"),
    )
    
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    answers = RichTextField(blank=True, null=True)
    tasks = RichTextField(blank=True, null=True)
    status = models.BooleanField(default=True)
    user = models.ForeignKey(User)
    songfile = models.FileField(upload_to='songs', blank=True)
    create_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
# Create your models here.
