from django import forms
from .models import UserForm


class UserForms(forms.ModelForm):
    class Meta:
        model = UserForm
        fields = ['first_name', 'last_name', 'email', 'age', 'address']
