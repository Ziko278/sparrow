from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(ParentsModel)
admin.site.register(StaffModel)
admin.site.register(StudentsModel)
admin.site.register(ClassesModel)