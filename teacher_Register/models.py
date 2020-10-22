from django.db import models
# Create your models here.
Roles = (
        ('Admin','Admin'),
        ('user','user'),
        
                    )
Stats = (
        ('Pending','Pending'),
        ('Submited','Submited'),
        
                    )
class Teacher_Register(models.Model):
    Teacher_Name = models.CharField(max_length=40, null = True)	
    Email = models.EmailField(null = True)	
    Mobile = models.CharField(max_length=12,null = True)
    Status = models.CharField(choices = Stats, max_length=12,null = True)
class Teacher_signUp(models.Model):
    UserName = models.CharField(max_length=40, null = True)
    Password = models.CharField(max_length=40, null = True)
    Role = models.CharField(choices = Roles ,max_length=20, null = True) 	
    




