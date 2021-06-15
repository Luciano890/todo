from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Task
from django import forms
import datetime


class UserSignupForm(UserCreationForm):
  username = forms.CharField(
    label='',
    widget = forms.TextInput(
      attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Username'
      }
    )
  )
  email = forms.EmailField(
    label='',
    widget = forms.TextInput(
      attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Email'
      }
    )
  )
  password1 = forms.CharField(
    label='',
    widget = forms.PasswordInput(
      attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Password'
      }
    )
  )
  password2 = forms.CharField(
    label='',
    widget = forms.PasswordInput(
      attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Confirm password'
      }
    )
  )

  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']
    help_text = {k:"" for k in fields}


class UserLoginForm(AuthenticationForm):
  username = forms.CharField(
    label='',
    widget = forms.TextInput(
      attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Username'
      }
    )
  )
  password = forms.CharField(
    label='',
    widget = forms.PasswordInput(
      attrs={
        'class': 'form-control mb-4',
        'placeholder': 'Password'
      }
    )
  )

  class Meta:
    model = User
    fields = ['username', 'password']
    help_text = {k:"" for k in fields}


class TaskCreateForm(ModelForm):
  title = forms.CharField(
    label = 'Title',
    required=True,
    widget = forms.TextInput(
      attrs={
        'class': 'form-control',
        'max_length': 100,
        'placeholder': 'Pet'
      }
    )
  )
  description = forms.CharField(
    label='Description',
    widget = forms.TextInput(
      attrs={
        'class': 'form-control',
        'placeholder': 'Take out my pet'
      }
    )
  )
  expired_at = forms.DateTimeField(
    label='Finish date',
    required=True,
    initial=datetime.date.today,
    widget = forms.DateTimeInput(
      attrs={
        'type': 'datetime-local',
        'class': 'form-control',
      }
    )
  )


  class Meta:
    model = Task
    fields  = ('title', 'description', 'expired_at', 'category')


class TaskEditForm(ModelForm):
  task = forms.CharField(
    required=True,
    widget = forms.HiddenInput(
      attrs={
        'id':'taskEdit'
      }
    )
  )

  title = forms.CharField(
    label = 'Title',
    required=True,
    widget = forms.TextInput(
      attrs={
        'class': 'form-control',
        'max_length': 100,
        'placeholder': 'Pet',
        'id':'titleEdit'
      }
    )
  )
  description = forms.CharField(
    label='Description',
    widget = forms.TextInput(
      attrs={
        'class': 'form-control',
        'placeholder': 'Take out my pet',
        'id':'descriptionEdit'
      }
    )
  )
  expired_at = forms.DateTimeField(
    label='Finish date',
    required=True,
    initial=datetime.date.today,
    widget = forms.DateTimeInput(
      attrs={
        'type': 'datetime-local',
        'class': 'form-control',
        'id':'expiretAtEdit'
      }
    )
  )


  class Meta:
    model = Task
    fields  = ('id', 'title', 'description', 'expired_at', 'category')
