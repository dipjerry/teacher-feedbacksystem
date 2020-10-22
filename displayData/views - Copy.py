from django.shortcuts import render
from teacher_Register.models import Teacher_Register 
from ExcelMail.models import Teacher_Feedback
from django.db.models import Q ,Count, Case, When, IntegerField, Sum
from django.db import models
import pandas as pd
from rest_framework.views import APIView 
from rest_framework.response import Response
from django.core.mail import send_mail
import json
# Create your views here.
def display_Data(request):
    context = Teacher_Register.objects.all()
    return render(request,'displayData.html',{'context':context})
def teacher_Feedback(request, Teacher_Name):
    teacher_F = Teacher_Feedback.objects.filter(Teacher_Name = Teacher_Name)
    # data = pd.DataFrame(teacher_F)
    # For Seminar
    teacher_data = Teacher_Feedback.objects.filter(Teacher_Name = Teacher_Name).values( 
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
    'interaction', 
    'effectiveness')
    data1 = pd.DataFrame(teacher_data)
    # teacher_data_type10 = Teacher_Feedback.objects.filter(Teacher_Name = Teacher_Name).values( 
    # 'Seminar')
    # num_Seminar =len(teacher_data_type10)
    # seminar_unique_all = data1['Seminar'].nunique()
    num_Seminar = data1['Seminar'].count()
    # num_Seminarx =len(teacher_data_type10)
     
    # num_Seminar = seminar_unique_all  
  
    teacher_Fb = { Seminar['Seminar']:Seminar['Seminar__count'] * 100/num_Seminar for Seminar in teacher_data.annotate(Count('Seminar')) }
    # teacher_Fb = { Seminar['Seminar__count'] * 100/num_Seminar for Seminar in teacher_data_type10.annotate(Count('Seminar')) }
    # teacher_Fb_value = { Seminar['Seminar'] for Seminar in teacher_data_type10.annotate(Count('Seminar')) }
    json_string = json.dumps(teacher_Fb)
    # all_values_seminer = teacher_Fb.values() 
    # teacher_Fb_max = max(teacher_Fb, key= teacher_Fb.get)
    keys = json.dumps(list(teacher_Fb.keys()))
    values = json.dumps(list(teacher_Fb.values()))

    # find uniques value
    # Regular_Punctual_max = max(data1['Regular_Punctual'].value_counts(normalize=True))
    # Knowledge_max = max(data1['Knowledge'].value_counts(normalize=True))
    # Clarity_communication_max = max(data1['Clarity_communication'].value_counts(normalize=True))
    # helpStudent_max = max(data1['helpStudent'].value_counts(normalize=True))
    # presentation_max = max(data1['presentation'].value_counts(normalize=True))
    # motivatesInterest_max = max(data1['motivatesInterest'].value_counts(normalize=True))
    # co_opeartive_max = max(data1['co_opeartive'].value_counts(normalize=True))
    # newOutlook_max = max(data1['newOutlook'].value_counts(normalize=True))
    # checking_max = max(data1['checking'].value_counts(normalize=True))
    # Seminar_max = max(data1['Seminar'].value_counts(normalize=True))
    # interaction_max = max(data1['interaction'].value_counts(normalize=True))
    # effectiveness_max = max(data1['effectiveness'].value_counts(normalize=True))
    
    # max 

    Regular_Punctual_unique = data1['Regular_Punctual'].value_counts(normalize=True).nlargest(n=1)
    Knowledge_unique = data1['Knowledge'].value_counts(normalize=True).nlargest(n=1)
    Clarity_communication_unique = data1['Clarity_communication'].value_counts(normalize=True).nlargest(n=1)
    helpStudent_unique = data1['helpStudent'].value_counts(normalize=True).nlargest(n=1)
    presentation_unique = data1['presentation'].value_counts(normalize=True).nlargest(n=1)
    motivatesInterest_unique = data1['motivatesInterest'].value_counts(normalize=True).nlargest(n=1)
    co_opeartive_unique = data1['co_opeartive'].value_counts(normalize=True).nlargest(n=1)
    newOutlook_unique = data1['newOutlook'].value_counts(normalize=True).nlargest(n=1)
    checking_unique = data1['checking'].value_counts(normalize=True).nlargest(n=1)
    Seminar_unique = data1['Seminar'].value_counts(normalize=True)
    interaction_unique = data1['interaction'].value_counts(normalize=True).nlargest(n=1)
    effectiveness_unique = data1['effectiveness'].value_counts(normalize=True).nlargest(n=1)

    #unique 
    Regular_Punctual_unique_all = data1['Regular_Punctual'].unique()
    # Regular_Punctual_unique_all_no = (len(Regular_Punctual_unique_all),(data1['Regular_Punctual'].value_counts()))  
    Regular_Punctual_unique_all_no = (len(Regular_Punctual_unique_all))  
    



    # graph plot
    # .nlargest(n=1)
# pass data to templete
    context= {'teacher_F':teacher_F,
    'title':Teacher_Name,
    # 'teacher_Fb_value':teacher_Fb_value,
    # 'teacher_Fb_max':teacher_Fb_max,
    'teacher_Fb' : teacher_Fb , 
    # 'teacher_Pt_max':teacher_Pt_max,
    'data1' : data1.to_html(),
    'data1_desc' : data1.describe().to_html(),
    'Regular_Punctual_unique':Regular_Punctual_unique,  	
    'Knowledge_unique': Knowledge_unique, 
    'Clarity_communication_unique':Clarity_communication_unique,  
    'helpStudent_unique':helpStudent_unique,  
    'presentation_unique':presentation_unique, 
    'motivatesInterest_unique':motivatesInterest_unique,  
    'co_opeartive_unique':co_opeartive_unique,  
    'newOutlook_unique':newOutlook_unique,  
    'checking_unique':checking_unique, 
    'Seminar_unique':Seminar_unique, 
    'interaction_unique': interaction_unique, 
    'effectiveness_unique':effectiveness_unique,
    # for max 

    # 'Regular_Punctual_max':Regular_Punctual_max,  	
    # 'Knowledge_max': Knowledge_max, 
    # 'Clarity_communication_max':Clarity_communication_max,  
    # 'helpStudent_max':helpStudent_max,  
    # 'presentation_max':presentation_max, 
    # 'motivatesInterest_max':motivatesInterest_max,  
    # 'co_opeartive_max':co_opeartive_max,  
    # 'newOutlook_max':newOutlook_max,  
    # 'checking_max':checking_max, 
    # 'Seminar_max':Seminar_max, 
    # 'interaction_max': interaction_max, 
    # 'effectiveness_max':effectiveness_max,
    'Regular_Punctual_unique_all' : Regular_Punctual_unique_all,
    'Regular_Punctual_unique_all_no' : Regular_Punctual_unique_all_no,
    
    'json_string' : json_string,
    'keys' : keys,
    'values' : values,
    # 'num_Seminarx' : num_Seminarx,
    'num_Seminar' : num_Seminar

    }
    # teacher_data_type2 = Teacher_Feedback.objects.filter(Teacher_Name = Teacher_Name).values(  	
    # 'Knowledge', 
    # 'Clarity_communication',  
    # 'helpStudent',  
    # 'presentation',  
    # 'interaction', 
    # 'effectiveness' 
    # )
    # teacher_data_type3 = Teacher_Feedback.objects.filter(Teacher_Name = Teacher_Name).values(  	
    # 'Regular_Punctual'
    # )
    
    return render(request,'TeacherFeedbackReport.html',context)







