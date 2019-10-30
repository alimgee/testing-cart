from django import forms # built in
from django.contrib.auth.models import User # built in
from django.contrib.auth.forms import UserCreationForm # from built in
from users.models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() # creating email field 

    class Meta: # additional metadata for form
        model = User # using built in User model
        fields = ['username', 'email', 'password1', 'password2'] # addtional fields to user model

class UserUpdateForm(forms.ModelForm): # model form to update user
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm): # model form to update profile image
    class Meta:
        model = Profile
        fields = ['image']