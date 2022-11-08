from dataclasses import fields
from inspect import Attribute
from .models import *
from django.forms import ModelForm, Form
from django import forms

class TeamForm(ModelForm):
    
    
    class Meta:
        model = Profile
        fields = '__all__'
# here you used the models as the medium to create the user form since there is already an info about the demands for the form to be created with.
# it always best to used and also fast to work with as you dont need to code for the information you demand from the user.
class BookCreateForm(ModelForm):

    class Meta:
        model = Book
        fields = "__all__"
        # exclude = ['first_name'] this is used to remove some of the Attribute out of the models or what the user have to be required to input

class ConfirmForm(forms.Form):
    confirm = forms.BooleanField(label="confirm delete")


# This class is used to create a form in which you code for the form.
class UserInfoForm(forms.Form):
    first_name = forms.CharField(max_length=140)
    Last_name = forms.CharField(max_length=140)
    email = forms.EmailField()
    image = forms.ImageField()


#below form is for user signup page 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User 
"""instead of creating another models for the user, we used the already created django user models and made some modifications to it"""

class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SignupForm, self). __init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter Username '
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Password confirm'

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2") 
        """those are the fields we intent to used in the creation of the user page."""


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.fields['password'].widget.attrs['placeholder']= 'password'
        self.fields['username'].widget.attrs['placeholder']= 'Username'