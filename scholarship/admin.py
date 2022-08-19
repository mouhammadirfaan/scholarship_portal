from django.contrib import admin
from .models import StudentUser, Provider
# Register your models here.

admin.site.register(StudentUser),
admin.site.register(Provider)