from django.db import models
# Create your models here.
class Teacher_Feedback(models.Model):
    Rating_type_1 = (
        ('Always Regular & Punctual','Always Regular & Punctual'),
('Not always Regular & Punctual','Not always Regular & Punctual'),
('Not Regular & Punctual','Not Regular & Punctual')
                    )
    Rating_type_2 = (
        ('Excellent','Excellent'),
        ('VeryGood','VeryGood'),
        ('Good','Good'),
        ('Average','Average'),
        ('Poor','Poor')
            )
    Rating_type_3 = (
        ('Highly','Highly'),
        ('Moderate','Moderate'),
        ('Average','Average'),
        ('Poor','Poor')
                    )
    Rating_type_4 = (
        ('Affectionate','Affectionate'),
        ('Friendly','Friendly'),
        ('Formal','Formal'),
        ('Less concerned','Less concerned')
                    )
    Semester = models.CharField(max_length=25, null = True)	
    Branch = models.CharField(max_length=35, null = True)
    Subject_Title = models.CharField(max_length=75, null = True)	
    Teacher_Name = models.CharField(max_length=40, null = True)	
    Regular_Punctual = models.CharField(choices = Rating_type_1 , max_length=40,null = True)	
    Knowledge = models.CharField(choices = Rating_type_2 ,max_length=40, null = True)
    Clarity_communication = models.CharField(choices = Rating_type_2 ,max_length=20, null = True)
    helpStudent = models.CharField(choices = Rating_type_2 ,max_length=20, null = True)
    presentation = models.CharField(choices = Rating_type_2 ,max_length=20, null = True)
    motivatesInterest = models.CharField(choices = Rating_type_3 ,max_length=20, null = True)
    co_opeartive = models.CharField(choices = Rating_type_3 ,max_length=20, null = True)
    newOutlook = models.CharField(choices = Rating_type_3 ,max_length=20, null = True)
    checking = models.CharField(choices = Rating_type_3 ,max_length=20, null = True)
    Seminar = models.CharField(choices = Rating_type_3 ,max_length=20, null = True)

    Communication_LD = models.CharField(choices = Rating_type_2 ,max_length=20, null = True)
    Study_Material_LD = models.CharField(choices = Rating_type_2 ,max_length=20, null = True)
    Online_Class_LD = models.CharField(choices = Rating_type_2 ,max_length=20, null = True)
    Laboratory_LD = models.CharField(choices = Rating_type_2 ,max_length=20, null = True)
    Teaching_LD = models.CharField(choices = Rating_type_2 ,max_length=20, null = True)
    interaction = models.CharField(choices = Rating_type_4 ,max_length=20, null = True)
    effectiveness = models.CharField(choices = Rating_type_2 ,max_length=20, null = True)
    