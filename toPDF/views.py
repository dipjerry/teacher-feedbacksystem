from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect 
from django.views.generic import View
from django.template.loader import get_template
from teacher_Register.models import Teacher_Register 
from ExcelMail.models import Teacher_Feedback
from django.db.models import Q ,Count, Case, When, IntegerField, Sum
from django.db import models
import pandas as pd
from rest_framework.views import APIView 
from rest_framework.response import Response
import os
from django.template.loader import render_to_string, get_template
# #pisa is a html2pdf converter using the ReportLab Toolkit,
# #the HTML5lib and pyPdf.
from xhtml2pdf import pisa  
from rest_framework.renderers import BaseRenderer
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt 
import io
# import xlwt
import urllib, base64
from matplotlib import pylab
from pylab import *
import PIL
import PIL.Image
from io import *
from django.http import FileResponse
import json
import numpy as np
from FinalProject.settings import EMAIL_HOST_USER
from django.core.mail import EmailMessage , BadHeaderError
from .form import FeedbackForm
from displayData.views import teacher_Feedback
from django.contrib import messages


# config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")

def render_to_pdf(request, media_type=None, renderer_context=None):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            Remark = request.POST.get("remark", None)
            Teacher_Name = request.POST.get("tName", None)
            t = Teacher_Register.objects.get(Teacher_Name =Teacher_Name)
    # # content start
        x = t.Email   
        if t.Status == 'Submited':
            messages.info(request,'email already sent')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
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
        Regular_Punctual_unique = list(Regular_Punctual_data.to_dict())
        Knowledge_unique = list(Knowledge_data.to_dict())
        Clarity_communication_unique = list(Clarity_communication_data.to_dict())
        helpStudent_unique = list(helpStudent_data.to_dict())
        presentation_unique = list(presentation_data.to_dict())
        motivatesInterest_unique = list(motivatesInterest_data.to_dict())
        co_opeartive_unique = list(co_opeartive_data.to_dict())
        newOutlook_unique = list(newOutlook_data.to_dict())
        checking_unique = list(checking_data.to_dict())
        seminar_unique = list(seminar_data.to_dict())
        interaction_unique = list(interaction_data.to_dict())
        effectiveness_unique = list(effectiveness_data.to_dict())
        # effectiveness_unique_m = data1['effectiveness'].value_counts(normalize=True).nlargest(n=1)
        # effectiveness_unique_max = effectiveness_unique_m.to_string(index=False) 
        
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
        if Regular_Punctual_M_d >= 33 and Regular_Punctual_M_d <= 66:
            Regular_Punctual_M_k = 'Always Regular & Punctual'
        elif Regular_Punctual_M_d >= 66 and Regular_Punctual_M_d < 100:
            Regular_Punctual_M_k = 'Not always Regular & Punctual'
        elif Regular_Punctual_M_d == 100:
            Regular_Punctual_M_k = 'Always Regular & Punctual'
        else:    
            Regular_Punctual_M_k = 'None'

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

        interaction_M_d = ((data1['value11'].sum() * 100) / (data1['value11'].count() * score1_max)).round(1) 
        if interaction_M_d >= 20 and interaction_M_d <= 40:
            interaction_M_k = 'Poor'
        elif interaction_M_d >= 40 and interaction_M_d <= 60:
            interaction_M_k = 'Average'
        elif interaction_M_d >= 60 and interaction_M_d <= 80:
            interaction_M_k= 'Good'
        elif interaction_M_d >= 80 and interaction_M_d < 100:
            interaction_M_k = 'Very Good'
        elif interaction_M_d == 100:
            interaction_M_k = 'Excellent'
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

        helpStudent_M_d = ((data1['value12'].sum() * 100) / (data1['value12'].count() * score1_max)).round(1)
        if helpStudent_M_d >= 20 and helpStudent_M_d <= 40:
            helpStudent_M_k = 'Poor'
        elif helpStudent_M_d >= 40 and helpStudent_M_d <= 60:
            helpStudent_M_k = 'Average'
        elif helpStudent_M_d >= 60 and helpStudent_M_d <= 80:
            helpStudent_M_k= 'Good'
        elif helpStudent_M_d >= 80 and effectiveness_M_d < 100:
            helpStudent_M_k = 'Very Good'
        elif helpStudent_M_d == 100:
            helpStudent_M_k = 'Excellent'
        else:
            helpStudent_M_k = 'None'

        presentation_M_d = ((data1['value5'].sum() * 100) / (data1['value5'].count() * score1_max)).round(1) 
        if presentation_M_d >= 20 and presentation_M_d <= 40:
            presentation_M_k = 'Poor'
        elif Knowledge_M_d >= 40 and presentation_M_d <= 60:
            presentation_M_k = 'Average'
        elif Knowledge_M_d >= 60 and presentation_M_d <= 80:
            presentation_M_k= 'Good'
        elif presentation_M_d >= 80 and presentation_M_d < 100:
            presentation_M_k = 'Very Good'
        elif presentation_M_d == 100:
            presentation_M_k = 'Excellent'
        else:
            presentation_M_k = 'None'
        
        # Creating Graphs for pdf
        #Regular and punctual graph
        fig1 = plt.barh(Regular_Punctual_unique, Regular_Punctual_data,  height=0.3,  align = 'center')
        plt.tight_layout()
        buffer1 = BytesIO()
        plt.savefig(buffer1, format='png')
        buffer1.seek(0)
        image_png1 = buffer1.getvalue()
        buffer1.close()
        graphic1 = base64.b64encode(image_png1).decode('utf-8')
        plt.close()
        # Knowledge 
        fig2 = plt.barh(Knowledge_unique, Knowledge_data,   height=0.3, align = 'center')
        plt.tight_layout()
        buffer2 = BytesIO()
        plt.savefig(buffer2, format='png')
        buffer2.seek(0)
        image_png2 = buffer2.getvalue()
        buffer2.close()
        graphic2 = base64.b64encode(image_png2).decode('utf-8')
        plt.close()
        #clarity
        fig3 = plt.barh(Clarity_communication_unique, Clarity_communication_data,  height=0.3, align = 'center')
        plt.tight_layout()
        buffer3 = BytesIO()
        plt.savefig(buffer3, format='png')
        buffer3.seek(0)
        image_png3 = buffer3.getvalue()
        buffer3.close()
        graphic3 = base64.b64encode(image_png3).decode('utf-8')
        plt.close()
        # help student
        fig4 = plt.barh(helpStudent_unique, helpStudent_data,  height=0.3, align = 'center')
        plt.tight_layout()
        buffer4 = BytesIO()
        plt.savefig(buffer4, format='png')
        buffer4.seek(0)
        image_png4 = buffer4.getvalue()
        buffer4.close()
        graphic4 = base64.b64encode(image_png4).decode('utf-8')
        plt.close()
        #presentation
        fig5 = plt.barh(presentation_unique, presentation_data,  height=0.3, align = 'center')
        plt.tight_layout()
        buffer5 = BytesIO()
        plt.savefig(buffer5, format='png')
        buffer5.seek(0)
        image_png5 = buffer5.getvalue()
        buffer5.close()
        graphic5 = base64.b64encode(image_png5).decode('utf-8')
        plt.close()
        # motivate interest
        fig6 = plt.barh(motivatesInterest_unique, motivatesInterest_data,  height=0.3, align = 'center')
        plt.tight_layout()
        buffer6 = BytesIO()
        plt.savefig(buffer6, format='png')
        buffer6.seek(0)
        image_png6 = buffer6.getvalue()
        buffer6.close()
        graphic6 = base64.b64encode(image_png6).decode('utf-8')
        plt.close()
        # co-operative
        fig7 = plt.barh(co_opeartive_unique, co_opeartive_data,  height=0.3, align = 'center')
        plt.tight_layout()
        buffer7 = BytesIO()
        plt.savefig(buffer7, format='png')
        buffer7.seek(0)
        image_png7 = buffer7.getvalue()
        buffer7.close()
        graphic7 = base64.b64encode(image_png7).decode('utf-8')
        plt.close()
        # new outlook
        fig8 = plt.barh(newOutlook_unique, newOutlook_data, height=0.3,align = 'center')
        plt.tight_layout()
        buffer8 = BytesIO()
        plt.savefig(buffer8, format='png')
        buffer8.seek(0)
        image_png8 = buffer8.getvalue()
        buffer8.close()
        graphic8 = base64.b64encode(image_png8).decode('utf-8')
        plt.close()
        #9 Checking
        fig9 = plt.barh(checking_unique, checking_data,  height=0.3, align = 'center')
        plt.tight_layout()
        buffer9 = BytesIO()
        plt.savefig(buffer9, format='png')
        buffer9.seek(0)
        image_png9 = buffer9.getvalue()
        buffer9.close()
        graphic9 = base64.b64encode(image_png9).decode('utf-8')
        plt.close()
        # seminar
        fig10 = plt.barh(seminar_unique, seminar_data,  height=0.3, align = 'center')
        plt.tight_layout()
        buffer10 = BytesIO()
        plt.savefig(buffer10, format='png')
        buffer10.seek(0)
        image_png10 = buffer10.getvalue()
        buffer10.close()
        graphic10 = base64.b64encode(image_png10).decode('utf-8')
        plt.close()
        # interection
        fig11 = plt.barh(interaction_unique, interaction_data,  height=0.3, align = 'center')
        plt.tight_layout()
        buffer11 = BytesIO()
        plt.savefig(buffer11, format='png')
        buffer11.seek(0)
        image_png11 = buffer11.getvalue()
        buffer11.close()
        graphic11 = base64.b64encode(image_png11).decode('utf-8')
        plt.close()
        # effectivness
        fig12 = plt.barh(effectiveness_unique, effectiveness_data,  height=0.3, align = 'center')
        plt.tight_layout()
        buffer12 = BytesIO()
        plt.savefig(buffer12, format='png')
        buffer12.seek(0)
        image_png12 = buffer12.getvalue()
        buffer12.close()
        graphic12 = base64.b64encode(image_png12).decode('utf-8')
        plt.close()


        context = {
        'Teacher_Name':Teacher_Name,
        # 'effectiveness_unique_max':effectiveness_unique_max,
        # 'teacher_Pt_max':teacher_Pt_max,
        'data1' : data1.to_html(),
        'data1_desc' : data1.describe().to_html(),

        'graphic1':graphic1,
        'graphic2':graphic2,
        'graphic3':graphic3,
        'graphic4':graphic4,
        'graphic5':graphic5,
        'graphic6':graphic6,
        'graphic7':graphic7,
        'graphic8':graphic8,
        'graphic9':graphic9,
        'graphic10':graphic10,
        'graphic11':graphic11,
        'graphic12':graphic12,
        'Remark' : Remark,
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
        'x' : x,
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
        }
        t.Status = "Submited"  # change field
        t.save() # this will update only
    # working pdf
        media_type = 'application/pdf'
        format = 'pdf'
        charset = 'utf-8'
        template = get_template('TeacherFeedbackReportpdf.html')
        html  = template.render(context)
        result = BytesIO()
    #      #This part will create the pdf.
        pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
        if not pdf.err:
            response = HttpResponse(result.getvalue())
            response['Content-Disposition'] = 'filename="Feedback.pdf"'
           
            subject = 'Your Monthly feedback'
            message = 'Here is your feed back for the month of ...........'
            recepient = x
            if subject and message and recepient:
                try:
                    send_mail =EmailMessage (subject, 
                    message, EMAIL_HOST_USER, [recepient])
                    send_mail.attach('Feedback.pdf', result.getvalue() , 'application/pdf')
                    send_mail.send()
                except BadHeaderError:
                    return HttpResponce('Invalid Header')
                # return render(request, 'success.html', {'recepient': recepient})
                messages.info(request,'email sent')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            return HttpResponse(result.getvalue(), content_type='application/pdf')
        # return render(request, 'success.html', {'recepient': recepient})
        return HttpResponse(result.getvalue(), content_type='application/pdf')
        

