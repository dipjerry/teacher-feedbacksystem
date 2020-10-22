from django.urls import path
from .import views


urlpatterns = [
    path("display_Data",views.display_Data, name="display_Data"),
    path("teacher_Feedback/<str:Teacher_Name>",views.teacher_Feedback),
    path("teacher_DataEdit/<str:Teacher_Name>",views.teacher_DataEdit , name = "teacher_DataEdit"),
   
 ]