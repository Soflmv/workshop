from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'phone']

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['email'].help_text = ''
        self.fields['first_name'].help_text = ''
        self.fields['last_name'].help_text = ''
        self.fields['phone'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'phone']



