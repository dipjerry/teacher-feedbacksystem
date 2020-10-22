from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("login_user", views.login_user, name="login_user"),
    path("logout", views.logout, name="logout"),    
    path("reset", views.reset, name="reset"),    
    path("home", views.home, name="home"),
    

]