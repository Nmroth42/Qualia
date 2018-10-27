from django import forms
from ckeditor.widgets import CKEditorWidget

from django.contrib.auth.models import User
from taskerapp.models import Profile
from taskerapp.models import Gig


class UserForm(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ("username", "password", "first_name", "last_name", "email")

class UserFormForEdit(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "username")
        

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("status","logo", )

class GigForm(forms.ModelForm):
    description = forms.CharField(label='Description', widget=forms.Textarea(attrs={'class': 'ckeditor'}))
    class Meta:
        model = Gig
        fields = ["title", "category", "description", "price", "photo", "status"]