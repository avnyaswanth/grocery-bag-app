from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.models import fields_for_model

class CreateNewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']