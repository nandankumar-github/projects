from dataclasses import fields
from django import forms
from school import models
from school.models import StudentModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext, gettext_lazy as _


class StudentForm(forms.ModelForm):
    class Meta:
        model=StudentModel
        fields=['id','name','roll','school','address']

class Profile(UserCreationForm):
     error_messages = {
        'password_mismatch': _("Password you have intered is inccorect"),
    }
     password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput,
    )
     password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput,
        strip=False,
    )
     class Meta:
        model=User
        fields=['username','email','first_name','last_name']



