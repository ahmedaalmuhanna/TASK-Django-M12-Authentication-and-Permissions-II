
from dataclasses import field
from pyexpat import model
from tkinter import Widget
from django import forms
from django.contrib.auth import get_user_model

User =get_user_model


class RegistrationForm (forms.ModelForms):
    class Meta:
        model = User
        field =['username','password']
        Widget ={
            
            "password" : forms.PasswordInput()
        }