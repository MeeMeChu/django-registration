from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from app_users.models import Profile

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ("email", )

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name","last_name")

class ExtendedProfileForm(forms.ModelForm):
    prefix = 'extended'
    class Meta:
        model = Profile
        fields = ("phone", )
        labels = {
            "phone" : "เบอร์โทรศัพท์",
        }