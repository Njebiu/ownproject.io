from django.contrib import admin
from .models import StudentsModels, StudentDetailsModels

# Register your models here.
admin.site.register(StudentsModels)
admin.site.register(StudentDetailsModels)


