from django.contrib import admin
from University.apps.academicManagement.models import *

# Register your models here.
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Enrollment)