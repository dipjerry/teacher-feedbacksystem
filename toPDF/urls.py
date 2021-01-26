from django.urls import path
from .import views


urlpatterns = [
   path('render_to_pdf', views.render_to_pdf),
   
    
 ]