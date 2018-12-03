from django import forms
from ckeditor.widgets import CKEditorWidget

from django.contrib.auth.models import User
from taskerapp.models import Profile
from taskerapp.models import Gig
from taskerapp.models import Comment


class UserForm(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ("username", "password", "first_name", "last_name", "email")

class UserFormForEdit(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email",)
        

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()

class ProfileFormForEdit(forms.ModelForm):
    status = forms.CharField(label='About me', widget=forms.Textarea)
    class Meta:
        model = Profile
        fields = ("status","logo",)


class GigForm(forms.ModelForm):
    tasks = forms.CharField(label='Tasks', widget=forms.Textarea(attrs={'class': 'ckeditor'} ))
    answers = forms.CharField(label='Answers', widget=forms.Textarea(attrs={'class': 'ckeditor'}))
    songfile = forms.FileField(label='Speaking', required=False)
    class Meta:
        model = Gig
        fields = ["category", "tasks", "answers", "songfile", "status"]

class CommentForm(forms.Form):
    
    
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'ckeditor'} ))
   

   