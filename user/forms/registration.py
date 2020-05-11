from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import account

class RegistrationForm(UserCreationForm):
