from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import userAdmin

from .models import CustomUser


admin.site.register(CustomUser)

