from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ('city', 'phone')

    fieldsets = UserAdmin.fieldsets + (
        ('Custom Info', {'fields': ('city', 'state', 'address', 'phone')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

