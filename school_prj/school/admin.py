from django.contrib import admin
from school.models import CityModel, SchoolModel, StudentModel

# Register your models here.
admin.site.register(CityModel)
admin.site.register(SchoolModel)
admin.site.register(StudentModel)
