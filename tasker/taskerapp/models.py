# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Profile(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE, )
    status = models.CharField(max_length=500,  blank=True, null=True)
    logo = models.ImageField(upload_to='task_logo/', blank=True, null=True)
    
    def __str__(self):
        return self.name

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
        return self.category

    

class Comment(models.Model):
    user = models.ForeignKey(User)
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.name
# Create your models here.
