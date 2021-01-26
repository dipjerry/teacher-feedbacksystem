from django.urls import path
from .import views

urlpatterns = [

    path("teacher_upload",views.teacher_upload, name="teacher_upload"),
    path("generate_users",views.generate_users, name="generate_users")
]