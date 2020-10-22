from django.shortcuts import render
from teacher_Register.models import Teacher_Register 
from ExcelMail.models import Teacher_Feedback
from django.db.models import Q ,Count, Case, When, IntegerField, Sum
from django.db import models
import pandas as pd
import numpy as np
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
    # for counting nosd of records
    data1 = pd.DataFrame(teacher_data)
    # UNIQUE VALUES COUNTS 
    Regular_Punctual_data = data1['Regular_Punctual'].value_counts(normalize=True)
    Knowledge_data = data1['Knowledge'].value_counts(normalize=True)
    Clarity_communication_data = data1['Clarity_communication'].value_counts(normalize=True)
    helpStudent_data = data1['helpStudent'].value_counts(normalize=True)    
    presentation_data = data1['presentation'].value_counts(normalize=True)
    motivatesInterest_data = data1['motivatesInterest'].value_counts(normalize=True)
    co_opeartive_data = data1['co_opeartive'].value_counts(normalize=True)
    newOutlook_data = data1['newOutlook'].value_counts(normalize=True)
    checking_data = data1['checking'].value_counts(normalize=True)
    seminar_data = data1['Seminar'].value_counts(normalize=True)
    interaction_data = data1['interaction'].value_counts(normalize=True)
    effectiveness_data = data1['effectiveness'].value_counts(normalize=True)
      
    #unique Records  
    Regular_Punctual_unique = data1['Regular_Punctual'].unique()
    Knowledge_unique = data1['Knowledge'].unique()
    Clarity_communication_unique = data1['Clarity_communication'].unique()
    helpStudent_unique = data1['helpStudent'].unique()
    presentation_unique = data1['presentation'].unique()
    motivatesInterest_unique = data1['motivatesInterest'].unique()
    co_opeartive_unique = data1['co_opeartive'].unique()
    newOutlook_unique = data1['newOutlook'].unique()
    checking_unique = data1['checking'].unique()
    seminar_unique = data1['Seminar'].unique()
    interaction_unique = data1['interaction'].unique()
    effectiveness_unique = data1['effectiveness'].unique()
    
    # DATA and LABEL for the graph in JSON format
    # FOR SEMINAR 
    Seminar_G = json.dumps(seminar_data.tolist())
    Seminar_L = json.dumps(list(seminar_data.to_dict()))
    # FOR Regular_Punctual 
    Regular_Punctual_G = json.dumps(Regular_Punctual_data.tolist())
    Regular_Punctual_L = json.dumps(list(Regular_Punctual_data.to_dict()))
    # For Knowledge
    Knowledge_G = json.dumps(Knowledge_data.tolist())
    Knowledge_L = json.dumps(list(Knowledge_data.to_dict())) 
    # for Clarity_communication
    Clarity_communication_G = json.dumps(Clarity_communication_data.tolist())
    Clarity_communication_L = json.dumps(list(Clarity_communication_data.to_dict()))  
    # for helpStudent
    helpStudent_G = json.dumps(helpStudent_data.tolist())
    helpStudent_L = json.dumps(list(helpStudent_data.to_dict()))  
    # presentation
    presentation_G = json.dumps(presentation_data.tolist())
    presentation_L = json.dumps(list(presentation_data.to_dict())) 
    # motivatesInterest
    motivatesInterest_G = json.dumps(motivatesInterest_data.tolist())
    motivatesInterest_L = json.dumps(list(motivatesInterest_data.to_dict()))  
    # co_opeartive
    co_opeartive_G = json.dumps(co_opeartive_data.tolist())
    co_opeartive_L = json.dumps(list(co_opeartive_data.to_dict()))
    # newOutlook 
    newOutlook_G = json.dumps(newOutlook_data.tolist())
    newOutlook_L = json.dumps(list(newOutlook_data.to_dict()))
    # checking 
    checking_G = json.dumps(checking_data.tolist())
    checking_L = json.dumps(list(checking_data.to_dict()))
    # interaction 
    interaction_G = json.dumps(interaction_data.tolist())
    interaction_L = json.dumps(list(interaction_data.to_dict()))
    # 'effectiveness 
    effectiveness_G = json.dumps(effectiveness_data.tolist())
    effectiveness_L = json.dumps(list(effectiveness_data.to_dict()))
#     effectiveness_Gl = effectiveness_data.tolist()
#     effectiveness_Ll = effectiveness_unique.tolist()
    #  Max values
    # Regular_Punctual_M_d = max(Regular_Punctual_data.mul(100).round(1).astype(str)+'%')
    # Regular_Punctual_M_k = max(Regular_Punctual_data.to_dict(), key=Regular_Punctual_data.to_dict().get)
    
    # Knowledge_M_d = max(Knowledge_data.mul(100).round(1).astype(str)+'%')
    # Knowledge_M_k = max(Knowledge_data.to_dict(), key=Knowledge_data.to_dict().get)
    
    # Clarity_communication_M_d = max(co_opeartive_data.mul(100).round(1).astype(str)+'%')
    # Clarity_communication_M_k = max(Clarity_communication_data.to_dict(), key=Clarity_communication_data.to_dict().get)
    
    # helpStudent_M_d = max(helpStudent_data.mul(100).round(1).astype(str)+'%')
    # helpStudent_M_k = max(helpStudent_data.to_dict(), key=helpStudent_data.to_dict().get)
    
    # presentation_M_d = max(presentation_data.mul(100).round(1).astype(str)+'%')
    # presentation_M_k = max(presentation_data.to_dict(), key=presentation_data.to_dict().get)
    
    # motivatesInterest_M_d = max(motivatesInterest_data.mul(100).round(1).astype(str)+'%')
    # motivatesInterest_M_k = max(motivatesInterest_data.to_dict(), key=motivatesInterest_data.to_dict().get)
    
    # co_opeartive_M_d = max(co_opeartive_data.mul(100).round(1).astype(str)+'%')
    # co_opeartive_M_k = max(co_opeartive_data.to_dict(), key=co_opeartive_data.to_dict().get)
    
    # newOutlook_M_d = max(newOutlook_data.mul(100).round(1).astype(str)+'%')
    # newOutlook_M_k = max(newOutlook_data.to_dict(), key=newOutlook_data.to_dict().get)
    
    # checking_M_d = max(checking_data.mul(100).round(1).astype(str)+'%')
    # checking_M_k = max(checking_data.to_dict(), key=checking_data.to_dict().get)
    
    # interaction_M_d = max(interaction_data.mul(100).round(1).astype(str)+'%')
    # interaction_M_k = max(interaction_data.to_dict(), key=interaction_data.to_dict().get)
    
    # effectiveness_M_d = max(effectiveness_data.mul(100).round(1).astype(str)+'%')
    # effectiveness_M_k = max(effectiveness_data.to_dict(), key=effectiveness_data.to_dict().get)
    
    # Seminar_M_d = max(seminar_data.mul(100).round(1).astype(str)+'%')
    # Seminar_M_k = max(seminar_data.to_dict(), key=seminar_data.to_dict().get)
    
    # define and map score

    Score1 = {'Excellent':5,'Very Good':4,'Good':3,'Average':2,'Poor':1}
    Score2 = {'Highly':4,'Moderate':3,'Average':2,'Poor':1}
    Score3 = {'Always Regular & Punctual':3, 'Not always Regular & Punctual':2, 'Not Regular & Punctual':1}
    score1_max = 5
    score2_max = 4
    score3_max = 3

    data1['value1'] = data1['Regular_Punctual'].map(Score3)
    data1['value2'] = data1['Knowledge'].map(Score1)
    data1['value3'] = data1['Clarity_communication'].map(Score1)
    data1['value4'] = data1['helpStudent'].map(Score1)
    data1['value5'] = data1['presentation'].map(Score1)
    data1['value6'] = data1['motivatesInterest'].map(Score2)
    data1['value7'] = data1['co_opeartive'].map(Score2)
    data1['value8'] = data1['newOutlook'].map(Score2)
    data1['value9'] = data1['checking'].map(Score2)
    data1['value10'] = data1['Seminar'].map(Score2)
    data1['value11'] = data1['interaction'].map(Score1)
    data1['value12'] = data1['effectiveness'].map(Score1)
    # calculate score
    Regular_Punctual_M_d = ((data1['value1'].sum() * 100) / (data1['value1'].count() * score3_max)).round(1) 
    if Regular_Punctual_M_d >= 33 and Regular_Punctual_M_d < 66:
        Regular_Punctual_M_k = 'Always Regular & Punctual'
    elif Regular_Punctual_M_d >= 66 and Regular_Punctual_M_d < 100:
        Regular_Punctual_M_k = 'Not always Regular & Punctual'
    elif Regular_Punctual_M_d == 100:
        Regular_Punctual_M_k = 'Always Regular & Punctual'

    Knowledge_M_d = ((data1['value2'].sum() * 100) / (data1['value2'].count() * score1_max)).round(1) 
    if Knowledge_M_d >= 20 and Knowledge_M_d < 40:
        Knowledge_M_k = 'Poor'
    elif Knowledge_M_d >= 40 and Knowledge_M_d < 60:
        Knowledge_M_k = 'Average'
    elif Knowledge_M_d >= 60 and Knowledge_M_d < 80:
        Knowledge_M_k= 'Good'
    elif Knowledge_M_d >= 80 and Knowledge_M_d < 100:
        Knowledge_M_k = 'Very Good'
    elif Knowledge_M_d == 100:
        Knowledge_M_k = 'Excellent'

    Clarity_communication_M_d = ((data1['value3'].sum() * 100) / (data1['value3'].count() * score1_max)).round(1)
    if Clarity_communication_M_d >= 20 and Clarity_communication_M_d < 40:
        Clarity_communication_M_k = 'Poor'
    elif Clarity_communication_M_d >= 40 and Clarity_communication_M_d < 60:
        Clarity_communication_M_k = 'Average'
    elif Clarity_communication_M_d >= 60 and Clarity_communication_M_d < 80:
        Clarity_communication_M_k= 'Good'
    elif Clarity_communication_M_d >= 80 and Clarity_communication_M_d < 100:
        Clarity_communication_M_k = 'Very Good'
    elif Clarity_communication_M_d == 100:
        Clarity_communication_M_k = 'Excellent'
   
    helpStudent_M_d = ((data1['value4'].sum() * 100) / (data1['value4'].count() * score1_max)).round(1) 
    if helpStudent_M_d >= 20 and helpStudent_M_d < 40:
        helpStudent_M_k = 'Poor'
    elif helpStudent_M_d >= 40 and helpStudent_M_d < 60:
        helpStudent_M_k = 'Average'
    elif Knowledge_M_d >= 60 and helpStudent_M_d < 80:
        helpStudent_M_k= 'Good'
    elif helpStudent_M_d >= 80 and helpStudent_M_d < 100:
        helpStudent_M_k = 'Very Good'
    elif helpStudent_M_d == 100:
        helpStudent_M_k = 'Excellent'

    presentation_M_d = ((data1['value5'].sum() * 100) / (data1['value5'].count() * score1_max)).round(1) 
    if presentation_M_d >= 20 and presentation_M_d < 40:
        presentation_M_k = 'Poor'
    elif Knowledge_M_d >= 40 and presentation_M_d < 60:
        presentation_M_k = 'Average'
    elif Knowledge_M_d >= 60 and presentation_M_d < 80:
        presentation_M_k= 'Good'
    elif presentation_M_d >= 80 and presentation_M_d < 100:
        presentation_M_k = 'Very Good'
    elif presentation_M_d == 100:
        presentation_M_k = 'Excellent'

    motivatesInterest_M_d = ((data1['value6'].sum() * 100) / (data1['value6'].count() * score2_max)).round(1) 
    if motivatesInterest_M_d >= 25 and motivatesInterest_M_d < 50:
        motivatesInterest_M_k = 'Poor'
    elif motivatesInterest_M_d >= 50 and motivatesInterest_M_d < 75:
        motivatesInterest_M_k = 'Average'
    elif motivatesInterest_M_d >= 75 and motivatesInterest_M_d < 100:
        motivatesInterest_M_k = 'Moderate'
    elif motivatesInterest_M_d == 100:
        motivatesInterest_M_k = 'Highly'

    co_opeartive_M_d = ((data1['value7'].sum() * 100) / (data1['value7'].count() * score2_max)).round(1)
    if co_opeartive_M_d >= 25 and co_opeartive_M_d < 50:
        co_opeartive_M_k = 'Poor'
    elif co_opeartive_M_d >= 50 and co_opeartive_M_d < 75:
        co_opeartive_M_k = 'Average'
    elif co_opeartive_M_d >= 75 and co_opeartive_M_d < 100:
        co_opeartive_M_k = 'moderate'
    elif co_opeartive_M_d == 100:
        co_opeartive_M_k = 'Highly'

    newOutlook_M_d = ((data1['value8'].sum() * 100) / (data1['value8'].count() * score2_max)).round(1) 
    if newOutlook_M_d >= 25 and newOutlook_M_d < 50:
        newOutlook_M_k = 'Poor'
    elif newOutlook_M_d >= 50 and newOutlook_M_d < 75:
        newOutlook_M_k = 'Average'
    elif newOutlook_M_d >= 75 and newOutlook_M_d < 100:
        newOutlook_M_k = 'Moderate'
    elif newOutlook_M_d == 100:
        newOutlook_M_k = 'Highly'

    checking_M_d = ((data1['value9'].sum() * 100) / (data1['value9'].count() * score2_max)).round(1) 
    if checking_M_d >= 25 and checking_M_d < 50:
        checking_M_k = 'Poor'
    elif checking_M_d >= 50 and checking_M_d < 75:
        checking_M_k = 'Average'
    elif checking_M_d >= 75 and checking_M_d < 100:
        checking_M_k = 'Moderate'
    elif checking_M_d == 100:
        checking_M_k = 'Highly'

    Seminar_M_d = ((data1['value10'].sum() * 100) / (data1['value10'].count() * score2_max)).round(1) 
    if Seminar_M_d >= 25 and Seminar_M_d < 50:
        Seminar_M_k = 'Poor'
    elif Seminar_M_d >= 50 and Seminar_M_d < 75:
        Seminar_M_k = 'Average'
    elif Seminar_M_d >= 75 and Seminar_M_d < 100:
        Seminar_M_k = 'Moderate'
    elif Seminar_M_d == 100:
        Seminar_M_k = 'Highly'

    interaction_M_d = ((data1['value11'].sum() * 100) / (data1['value11'].count() * score1_max)).round(1) 
    if interaction_M_d >= 20 and interaction_M_d < 40:
        interaction_M_k = 'Poor'
    elif interaction_M_d >= 40 and interaction_M_d < 60:
        interaction_M_k = 'Average'
    elif interaction_M_d >= 60 and interaction_M_d < 80:
        interaction_M_k= 'Good'
    elif interaction_M_d >= 80 and interaction_M_d < 100:
        interaction_M_k = 'Very Good'
    elif interaction_M_d == 100:
        interaction_M_k = 'Excellent'

    effectiveness_M_d = ((data1['value12'].sum() * 100) / (data1['value12'].count() * score1_max)).round(1)
    if effectiveness_M_d >= 20 and effectiveness_M_d < 40:
        effectiveness_M_k = 'Poor'
    elif effectiveness_M_d >= 40 and effectiveness_M_d < 60:
        effectiveness_M_k = 'Average'
    elif effectiveness_M_d >= 60 and effectiveness_M_d < 80:
        effectiveness_M_k= 'Good'
    elif effectiveness_M_d >= 80 and effectiveness_M_d < 100:
        effectiveness_M_k = 'Very Good'
    elif effectiveness_M_d == 100:
        effectiveness_M_k = 'Excellent'

    # effectiveness_M_d = ((data1['value10'].sum() * 100) / (data1['value10'].count() * score1_max)).round(1).astype(str)+'%'

    
    context= {'teacher_F':teacher_F,
    'Teacher_Name':Teacher_Name,
    # 'teacher_Pt_max':teacher_Pt_max,
    # 'x' : x,
    'Regular_Punctual_unique':Regular_Punctual_unique,
    
    'data1' : data1.to_html(),
    'data1_desc' : data1.describe().to_html(),
    'Regular_Punctual_data':Regular_Punctual_data,  	
    'Knowledge_data': Knowledge_data, 
    'Clarity_communication_data':Clarity_communication_data,  
    'helpStudent_data':helpStudent_data,  
    'presentation_data':presentation_data, 
    'motivatesInterest_data':motivatesInterest_data,  
    'co_opeartive_data':co_opeartive_data,  
    'newOutlook_data':newOutlook_data,  
    'checking_data':checking_data, 
    'seminar_data':seminar_data, 
    'interaction_data': interaction_data, 
    'effectiveness_data':effectiveness_data,
    
    
    'seminar_unique' : seminar_unique,
    
    # FOR GRAPH 
    'Regular_Punctual_G' : Regular_Punctual_G,
    'Regular_Punctual_L' : Regular_Punctual_L,
    'Knowledge_G' :Knowledge_G , 
    'Knowledge_L' :Knowledge_L , 
    'Clarity_communication_G' :Clarity_communication_G,  
    'Clarity_communication_L' :Clarity_communication_L,  
    'helpStudent_G' : helpStudent_G,  
    'helpStudent_L' : helpStudent_L,  
    'presentation_G': presentation_G, 
    'presentation_L': presentation_L, 
    'motivatesInterest_G' : motivatesInterest_G,
    'motivatesInterest_L' : motivatesInterest_L,  
    'co_opeartive_G' : co_opeartive_G,  
    'co_opeartive_L' : co_opeartive_L,  
    'newOutlook_G' : newOutlook_G,  
    'newOutlook_L' : newOutlook_L,  
    'checking_G' : checking_G, 
    'checking_L' : checking_L, 
    'interaction_G' : interaction_G, 
    'interaction_L' : interaction_L, 
    'effectiveness_G' : effectiveness_G, 
    'effectiveness_L' : effectiveness_L,
    'Seminar_G' : Seminar_G, 
    'Seminar_L' : Seminar_L,
    # Max 
    'Seminar_M_d' : Seminar_M_d, 
    'Seminar_M_k' : Seminar_M_k, 
    'Regular_Punctual_M_d' : Regular_Punctual_M_d,
    'Regular_Punctual_M_k' : Regular_Punctual_M_k,
    'Knowledge_M_d' :Knowledge_M_d , 
    'Knowledge_M_k' :Knowledge_M_k , 
    'Clarity_communication_M_d' :Clarity_communication_M_d,  
    'Clarity_communication_M_k' :Clarity_communication_M_k,  
    'helpStudent_M_d' : helpStudent_M_d,  
    'helpStudent_M_k' : helpStudent_M_k,  
    'presentation_M_d': presentation_M_d, 
    'presentation_M_k': presentation_M_k, 
    'motivatesInterest_M_d' : motivatesInterest_M_d,
    'motivatesInterest_M_k' : motivatesInterest_M_k,  
    'co_opeartive_M_d' : co_opeartive_M_d,  
    'co_opeartive_M_k' : co_opeartive_M_k,  
    'newOutlook_M_d' : newOutlook_M_d,  
    'newOutlook_M_k' : newOutlook_M_k,  
    'checking_M_d' : checking_M_d, 
    'checking_M_k' : checking_M_k, 
    'interaction_M_d' : interaction_M_d, 
    'interaction_M_k' : interaction_M_k, 
    'effectiveness_M_d' : effectiveness_M_d, 
    'effectiveness_M_k' : effectiveness_M_k,

    # 'chart' : cht, 
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
