from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUserTitan, UserProfileTitan, News

class CustomUserCreationForm(UserCreationForm):
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput,
        error_messages={
            'password_mismatch': 'As senhas não coincidem. Por favor, tente novamente.',
        }
    )

    class Meta:
        model = CustomUserTitan
        fields = ('name', 'username', 'email', 'password1', 'password2')

class RegistrationCodeForm(forms.Form):
    registration_code = forms.CharField(widget=forms.PasswordInput)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfileTitan
        fields = ['profile_picture', 'bio']

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'text', 'media', 'video_url']