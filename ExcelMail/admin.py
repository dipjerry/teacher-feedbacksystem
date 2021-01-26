from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Teacher_Feedback
# Register your models here.
@admin.register(Teacher_Feedback)
class Teacher_FeedbackAdmin(ImportExportModelAdmin):
    list_display = (
    'Semester',	
    'Branch',  	
    'Subject_Title',
    'Teacher_Name', 
    'Regular_Punctual',  	
    'Knowledge', 
    'Clarity_communication',  
    'helpStudent',  
    'presentation', 
    'motivatesInterest',  
    'co_opeartive',  
    'newOutlook',  
    'checking', 
    'Seminar',
    'Communication_LD',
    'Study_Material_LD',
    'Online_Class_LD',
    'Laboratory_LD',
    'Teaching_LD', 
    'interaction', 
    'effectiveness' )
