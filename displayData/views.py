from django.shortcuts import render , redirect, get_object_or_404 , HttpResponseRedirect
from django.core.paginator import Paginator
from teacher_Register.models import Teacher_Register 
from ExcelMail.models import Teacher_Feedback
from django.db.models import Q ,Count, Case, When, IntegerField, Sum
from django.db import models
from django.contrib import messages
import pandas as pd
import numpy as np
from rest_framework.views import APIView 
from rest_framework.response import Response
from django.core.mail import send_mail
import json
from teacher_Register.models import Teacher_Register
from teacher_Register.forms import TeacherRegisterFields
# Create your views here.
def display_Data(request):
    context = Teacher_Register.objects.all()
    if context.count()==0:
        messages.info(request,'No records Exist')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:    
        return render(request,'displayData.html',{'context':context})
    
        

def data(Teacher_Name):
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
    'Communication_LD',
    'Study_Material_LD',
    'Online_Class_LD',
    'Laboratory_LD',
    'Teaching_LD', 
    'interaction', 
    'effectiveness'
    )
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

    Communication_LD_data = data1['Communication_LD'].value_counts(normalize=True)
    Study_Material_LD_data = data1['Study_Material_LD'].value_counts(normalize=True)
    Online_Class_LD_data = data1['Online_Class_LD'].value_counts(normalize=True)
    Laboratory_LD_data = data1['Laboratory_LD'].value_counts(normalize=True)
    Teaching_LD_data = data1['Teaching_LD'].value_counts(normalize=True)

    interaction_data = data1['interaction'].value_counts(normalize=True)
    effectiveness_data = data1['effectiveness'].value_counts(normalize=True)
      
    # DATA and LABEL for the graph in JSON format
    
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
    # FOR SEMINAR 
    Seminar_G = json.dumps(seminar_data.tolist())
    Seminar_L = json.dumps(list(seminar_data.to_dict()))
    # FOR Communication in lockdown 
    Communication_LD_G = json.dumps(Communication_LD_data.tolist())
    Communication_LD_L = json.dumps(list(Communication_LD_data.to_dict()))
    # FOR study material in lockdown 
    Study_Material_LD_G = json.dumps(Study_Material_LD_data.tolist())
    Study_Material_LD_L = json.dumps(list(Study_Material_LD_data.to_dict()))
    # FOR online class in lockdown 
    Online_Class_LD_G = json.dumps(Online_Class_LD_data.tolist())
    Online_Class_LD_L = json.dumps(list(Online_Class_LD_data.to_dict()))
    # FOR Laboratory in lockdown 
    Laboratory_LD_G = json.dumps(Laboratory_LD_data.tolist())
    Laboratory_LD_L = json.dumps(list(Laboratory_LD_data.to_dict()))
    # FOR Teaching in lockdown 
    Teaching_LD_G = json.dumps(Teaching_LD_data.tolist())
    Teaching_LD_L = json.dumps(list(Teaching_LD_data.to_dict()))
    # interaction 
    interaction_G = json.dumps(interaction_data.tolist())
    interaction_L = json.dumps(list(interaction_data.to_dict()))
    # 'effectiveness 
    effectiveness_G = json.dumps(effectiveness_data.tolist())
    effectiveness_L = json.dumps(list(effectiveness_data.to_dict()))

    # define and map score

    Score1 = {'Excellent':5,'Very Good':4,'Good':3,'Average':2,'Poor':1}
    Score2 = {'Highly':4,'Moderate':3,'Average':2,'Poor':1}
    Score3 = {'Always Regular & Punctual':3, 'Not always Regular & Punctual':2, 'Not Regular & Punctual':1}
    Score4 = {'Affectionate':4,'Friendly':3,'Formal':2,'Less concerned':1}
    score1_max = 5
    score2_max = 4
    score3_max = 3
    score4_max = 4

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
    data1['value11'] = data1['interaction'].map(Score4)
    data1['value12'] = data1['effectiveness'].map(Score1)

    data1['value13'] = data1['Communication_LD'].map(Score1)
    data1['value14'] = data1['Study_Material_LD'].map(Score1)
    data1['value15'] = data1['Online_Class_LD'].map(Score1)
    data1['value16'] = data1['Laboratory_LD'].map(Score1)
    data1['value17'] = data1['Teaching_LD'].map(Score1)

    # calculate score
    Regular_Punctual_M_d = ((data1['value1'].sum() * 100) / (data1['value1'].count() * score3_max)).round(1) 
    if Regular_Punctual_M_d >= 33 and Regular_Punctual_M_d <= 66:
        Regular_Punctual_M_k = 'Not Always Regular & Punctual'
    elif Regular_Punctual_M_d >= 66 and Regular_Punctual_M_d < 100:
        Regular_Punctual_M_k = 'Not always Regular & Punctual'
    elif Regular_Punctual_M_d == 100:
        Regular_Punctual_M_k = 'Always Regular & Punctual'
    else:    
        Regular_Punctual_M_k = 'None'
    x = data1['value1'].sum()

    Knowledge_M_d = ((data1['value2'].sum() * 100) / (data1['value2'].count() * score1_max)).round(1) 
    if Knowledge_M_d >= 20 and Knowledge_M_d <= 40:
        Knowledge_M_k = 'Poor'
    elif Knowledge_M_d >= 40 and Knowledge_M_d <= 60:
        Knowledge_M_k = 'Average'
    elif Knowledge_M_d >= 60 and Knowledge_M_d <= 80:
        Knowledge_M_k= 'Good'
    elif Knowledge_M_d >= 80 and Knowledge_M_d <= 100:
        Knowledge_M_k = 'Very Good'
    elif Knowledge_M_d == 100:
        Knowledge_M_k = 'Excellent'
    else:
        Knowledge_M_k = 'None'

    Clarity_communication_M_d = ((data1['value3'].sum() * 100) / (data1['value3'].count() * score1_max)).round(1)
    if Clarity_communication_M_d >= 20 and Clarity_communication_M_d <= 40:
        Clarity_communication_M_k = 'Poor'
    elif Clarity_communication_M_d >= 40 and Clarity_communication_M_d <= 60:
        Clarity_communication_M_k = 'Average'
    elif Clarity_communication_M_d >= 60 and Clarity_communication_M_d <= 80:
        Clarity_communication_M_k= 'Good'
    elif Clarity_communication_M_d >= 80 and Clarity_communication_M_d < 100:
        Clarity_communication_M_k = 'Very Good'
    elif Clarity_communication_M_d == 100:
        Clarity_communication_M_k = 'Excellent'
    else:
        Clarity_communication_M_k = 'None'

    helpStudent_M_d = ((data1['value4'].sum() * 100) / (data1['value4'].count() * score1_max)).round(1)
    if helpStudent_M_d >= 20 and helpStudent_M_d <= 40:
        helpStudent_M_k = 'Poor'
    elif helpStudent_M_d >= 40 and helpStudent_M_d <= 60:
        helpStudent_M_k = 'Average'
    elif helpStudent_M_d >= 60 and helpStudent_M_d <= 80:
        helpStudent_M_k= 'Good'
    elif helpStudent_M_d >= 80 and helpStudent_M_d < 100:
        helpStudent_M_k = 'Very Good'
    elif helpStudent_M_d == 100:
        helpStudent_M_k = 'Excellent'
    else:
        helpStudent_M_k = 'None'

    presentation_M_d = ((data1['value5'].sum() * 100) / (data1['value5'].count() * score1_max)).round(1) 
    if presentation_M_d >= 20 and presentation_M_d <= 40:
        presentation_M_k = 'Poor'
    elif presentation_M_d >= 40 and presentation_M_d <= 60:
        presentation_M_k = 'Average'
    elif presentation_M_d >= 60 and presentation_M_d <= 80:
        presentation_M_k= 'Good'
    elif presentation_M_d >= 80 and presentation_M_d < 100:
        presentation_M_k = 'Very Good'
    elif presentation_M_d == 100:
        presentation_M_k = 'Excellent'
    else:
        presentation_M_k = 'None'
    

    motivatesInterest_M_d = ((data1['value6'].sum() * 100) / (data1['value6'].count() * score2_max)).round(1) 
    if motivatesInterest_M_d >= 25 and motivatesInterest_M_d <= 50:
        motivatesInterest_M_k = 'Poor'
    elif motivatesInterest_M_d >= 50 and motivatesInterest_M_d <= 75:
        motivatesInterest_M_k = 'Average'
    elif motivatesInterest_M_d >= 75 and motivatesInterest_M_d < 100:
        motivatesInterest_M_k = 'Moderate'
    elif motivatesInterest_M_d == 100:
        motivatesInterest_M_k = 'Highly'
    else:
        motivatesInterest_M_k = 'None'

    co_opeartive_M_d = ((data1['value7'].sum() * 100) / (data1['value7'].count() * score2_max)).round(1)
    if co_opeartive_M_d >= 25 and co_opeartive_M_d <= 50:
        co_opeartive_M_k = 'Poor'
    elif co_opeartive_M_d >= 50 and co_opeartive_M_d <= 75:
        co_opeartive_M_k = 'Average'
    elif co_opeartive_M_d >= 75 and co_opeartive_M_d < 100:
        co_opeartive_M_k = 'moderate'
    elif co_opeartive_M_d == 100:
        co_opeartive_M_k = 'Highly'
    else:    
        co_opeartive_M_k = 'None'

    newOutlook_M_d = ((data1['value8'].sum() * 100) / (data1['value8'].count() * score2_max)).round(1) 
    if newOutlook_M_d >= 25 and newOutlook_M_d <= 50:
        newOutlook_M_k = 'Poor'
    elif newOutlook_M_d >= 50 and newOutlook_M_d <= 75:
        newOutlook_M_k = 'Average'
    elif newOutlook_M_d >= 75 and newOutlook_M_d < 100:
        newOutlook_M_k = 'Moderate'
    elif newOutlook_M_d == 100:
        newOutlook_M_k = 'Highly'
    else:    
        newOutlook_M_k = 'None'
        
    checking_M_d = ((data1['value9'].sum() * 100) / (data1['value9'].count() * score2_max)).round(1) 
    if checking_M_d >= 25 and checking_M_d <= 50:
        checking_M_k = 'Poor'
    elif checking_M_d >= 50 and checking_M_d <= 75:
        checking_M_k = 'Average'
    elif checking_M_d >= 75 and checking_M_d < 100:
        checking_M_k = 'Moderate'
    elif checking_M_d == 100:
        checking_M_k = 'Highly'
    else:
        checking_M_k = 'None'

    Seminar_M_d = ((data1['value10'].sum() * 100) / (data1['value10'].count() * score2_max)).round(1) 
    if Seminar_M_d >= 25 and Seminar_M_d <= 50:
        Seminar_M_k = 'Poor'
    elif Seminar_M_d >= 50 and Seminar_M_d <= 75:
        Seminar_M_k = 'Average'
    elif Seminar_M_d >= 75 and Seminar_M_d <= 100:
        Seminar_M_k = 'Moderate'
    elif Seminar_M_d == 100:
        Seminar_M_k = 'Highly'
    else:
        Seminar_M_k = 'None'

    interaction_M_d = ((data1['value11'].sum() * 100) / (data1['value11'].count() * score4_max)).round(1) 
    if interaction_M_d >= 20 and interaction_M_d <= 60:
        interaction_M_k = 'Less concerned'
    elif interaction_M_d >= 60 and interaction_M_d <= 80:
        interaction_M_k= 'Formal'
    elif interaction_M_d >= 80 and interaction_M_d < 100:
        interaction_M_k = 'Friendly'
    elif interaction_M_d == 100:
        interaction_M_k = 'Affectionate'
    else:
        interaction_M_k = 'None'

    effectiveness_M_d = ((data1['value12'].sum() * 100) / (data1['value12'].count() * score1_max)).round(1)
    if effectiveness_M_d >= 20 and effectiveness_M_d <= 40:
        effectiveness_M_k = 'Poor'
    elif effectiveness_M_d >= 40 and effectiveness_M_d <= 60:
        effectiveness_M_k = 'Average'
    elif effectiveness_M_d >= 60 and effectiveness_M_d <= 80:
        effectiveness_M_k= 'Good'
    elif effectiveness_M_d >= 80 and effectiveness_M_d < 100:
        effectiveness_M_k = 'Very Good'
    elif effectiveness_M_d == 100:
        effectiveness_M_k = 'Excellent'
    else:
        effectiveness_M_k = 'None'

    
    Communication_LD_M_d = ((data1['value13'].sum() * 100) / (data1['value13'].count() * score1_max)).round(1) 
    if Communication_LD_M_d >= 20 and Communication_LD_M_d <= 40:
        Communication_LD_M_k = 'Poor'
    elif Communication_LD_M_d >= 40 and Communication_LD_M_d <= 60:
        Communication_LD_M_k = 'Average'
    elif Communication_LD_M_d >= 60 and Communication_LD_M_d <= 80:
        Communication_LD_M_k= 'Good'
    elif Communication_LD_M_d >= 80 and Communication_LD_M_d < 100:
        Communication_LD_M_k = 'Very Good'
    elif Communication_LD_M_d == 100:
        Communication_LD_M_k = 'Excellent'
    
    Study_Material_LD_M_d = ((data1['value14'].sum() * 100) / (data1['value14'].count() * score1_max)).round(1) 
    if Study_Material_LD_M_d >= 20 and Study_Material_LD_M_d <= 40:
        Study_Material_LD_M_k = 'Poor'
    elif Study_Material_LD_M_d >= 40 and Study_Material_LD_M_d <= 60:
        Study_Material_LD_M_k = 'Average'
    elif Study_Material_LD_M_d >= 60 and Study_Material_LD_M_d <= 80:
        Study_Material_LD_M_k = 'Good'
    elif Study_Material_LD_M_d >= 80 and Study_Material_LD_M_d < 100:
        Study_Material_LD_M_k = 'Very Good'
    elif Study_Material_LD_M_d == 100:
        Study_Material_LD_M_k = 'Excellent'
    
    Online_Class_LD_M_d = ((data1['value15'].sum() * 100) / (data1['value15'].count() * score1_max)).round(1) 
    if Online_Class_LD_M_d >= 20 and Online_Class_LD_M_d <= 40:
        Online_Class_LD_M_k = 'Poor'
    elif Online_Class_LD_M_d >= 40 and Online_Class_LD_M_d <= 60:
        Online_Class_LD_M_k = 'Average'
    elif Online_Class_LD_M_d >= 60 and Online_Class_LD_M_d <= 80:
        Online_Class_LD_M_k = 'Good'
    elif Online_Class_LD_M_d >= 80 and Online_Class_LD_M_d < 100:
        Online_Class_LD_M_k = 'Very Good'
    elif Online_Class_LD_M_d == 100:
        Online_Class_LD_M_k = 'Excellent'
    
    Laboratory_LD_M_d = ((data1['value16'].sum() * 100) / (data1['value16'].count() * score1_max)).round(1) 
    if Laboratory_LD_M_d >= 20 and Laboratory_LD_M_d <= 40:
        Laboratory_LD_M_k = 'Poor'
    elif Laboratory_LD_M_d >= 40 and Laboratory_LD_M_d <= 60:
        Laboratory_LD_M_k = 'Average'
    elif Laboratory_LD_M_d >= 60 and Laboratory_LD_M_d <= 80:
        Laboratory_LD_M_k = 'Good'
    elif Laboratory_LD_M_d >= 80 and Laboratory_LD_M_d < 100:
        Laboratory_LD_M_k = 'Very Good'
    elif Laboratory_LD_M_d == 100:
        Laboratory_LD_M_k = 'Excellent'
    
    Teaching_LD_M_d = ((data1['value17'].sum() * 100) / (data1['value17'].count() * score1_max)).round(1) 
    if Teaching_LD_M_d >= 20 and Teaching_LD_M_d <= 40:
        Teaching_LD_M_k = 'Poor'
    elif Teaching_LD_M_d >= 40 and Teaching_LD_M_d <= 60:
        Teaching_LD_M_k = 'Average'
    elif Teaching_LD_M_d >= 60 and Teaching_LD_M_d <= 80:
        Teaching_LD_M_k = 'Good'
    elif Teaching_LD_M_d >= 80 and Teaching_LD_M_d < 100:
        Teaching_LD_M_k = 'Very Good'
    elif Teaching_LD_M_d == 100:
        Teaching_LD_M_k = 'Excellent'
    

    
    
    context= {'teacher_F':teacher_F,
    'Teacher_Name':Teacher_Name,
    # 'teacher_Pt_max':teacher_Pt_max,
    'x' : x,
    
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

    'Communication_LD_M_d' : Communication_LD_M_d ,
    'Communication_LD_M_k' : Communication_LD_M_k ,
    'Study_Material_LD_M_d' : Study_Material_LD_M_d ,
    'Study_Material_LD_M_k' : Study_Material_LD_M_k ,
    'Online_Class_LD_M_d' : Online_Class_LD_M_d ,
    'Online_Class_LD_M_k' : Online_Class_LD_M_k , 
    'Laboratory_LD_M_d' : Laboratory_LD_M_d,
    'Laboratory_LD_M_k' : Laboratory_LD_M_k,
    'Teaching_LD_M_d' : Teaching_LD_M_d,
    'Teaching_LD_M_k' :Teaching_LD_M_k,

    'Communication_LD_L':Communication_LD_L , 
    'Communication_LD_G' : Communication_LD_G,
    'Study_Material_LD_G' : Study_Material_LD_G , 
    'Study_Material_LD_L' : Study_Material_LD_L,
    'Online_Class_LD_L' : Online_Class_LD_L,
    'Online_Class_LD_G' : Online_Class_LD_G,
    'Laboratory_LD_L' : Laboratory_LD_L , 
    'Laboratory_LD_G' : Laboratory_LD_G ,
    'Teaching_LD_L' : Teaching_LD_L,
    'Teaching_LD_G' : Teaching_LD_G 
    }
    return context
    


def teacher_Feedback(request, Teacher_Name):
    context = data(Teacher_Name)
    return render(request,'TeacherFeedbackReport.html',context)
def teacher_Feedback_users(request, Teacher_Name):
    context = data(Teacher_Name)
    return render(request,'FeedbackReport_user.html',context)
    
    
def home(request):
    return render(request, 'index.html')

def teacher_DataEdit(request , Teacher_Name):
    dataEdit = get_object_or_404(Teacher_Register , Teacher_Name = Teacher_Name)
    if request.method == 'POST':
        form = TeacherRegisterFields(request.POST, instance = dataEdit)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TeacherRegisterFields(instance = dataEdit )
        return render(request, 'edit.html', {'form': form})
    
# def teacher_DataEdit(request , Teacher_Name):
#     return teacher_DataEditView(request , Teacher_Name ,Teacher_Register , TeacherRegisterFields)  


    
