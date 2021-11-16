from django import forms
from django.db.models import fields
from django.forms import widgets
from django.shortcuts import render
from . models import *
from django.contrib.auth.forms import UserCreationForm

#Notes Section
class NotesForm(forms.ModelForm):
    class Meta:
        model= Notes
        fields=['title','description']

# Homework Section
class DateInput(forms.DateInput):
    input_type = 'date'

class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        widgets = {'due':DateInput()}
        fields = ['subject','title','description','due','is_finished']

# YouTube Section
class DashboardForm(forms.Form):
    text = forms.CharField(max_length=200,label="Search :")

# To do Section
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title','is_finished'] 


# Register Section
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']       