from django.contrib import admin
from .models import UserForm
from django.contrib.auth.models import Group, User

# Register your models here.

# Unregister Group
admin.site.unregister(Group)

# Register UserForm 
admin.site.register(UserForm)