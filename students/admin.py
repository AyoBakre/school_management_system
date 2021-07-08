from django.contrib import admin

# Register your models here.
from students.models import *


admin.site.register(BioData)
admin.site.register(ClassName)
admin.site.register(ClassTeacher)
admin.site.register(Department)
