from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import UserProfile
from core.BootstrapFormMixin import BootstrapFormMixin


class SignUpForm(UserCreationForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_form()


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_picture',)
