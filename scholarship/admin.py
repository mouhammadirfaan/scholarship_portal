from django.contrib import admin
from .models import StudentUser, Provider, AddScholarship
# Register your models here.

admin.site.register(StudentUser),
admin.site.register(Provider),
admin.site.register(AddScholarship),
# admin.site.register(StudentProfile)

