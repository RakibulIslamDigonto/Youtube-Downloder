from django.contrib import admin
from .models import CreateUser


# Register your models here.
@admin.register(CreateUser)
class UserAdmin(admin.ModelAdmin):
    display = ('id', 'name', 'email', 'password')