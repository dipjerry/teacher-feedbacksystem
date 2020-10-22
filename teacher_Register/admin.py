from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Teacher_Register, Teacher_signUp

# Register your models here.
@admin.register(Teacher_Register)
class Teacher_RegisterAdmin(ImportExportModelAdmin):
    list_display = (
    'Teacher_Name',	
    'Email',  	
    'Mobile',
    'Status'
     )

@admin.register(Teacher_signUp)
class Teacher_signUpAdmin(ImportExportModelAdmin):
    list_display = (
    'UserName',	
    'Password',
    'Role'
     )
