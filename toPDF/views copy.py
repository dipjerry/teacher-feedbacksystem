from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect 
from django.views.generic import View
#importing get_template from loader
from django.template.loader import get_template
from teacher_Register.models import Teacher_Register 
from ExcelMail.models import Teacher_Feedback
from django.db.models import Q ,Count, Case, When, IntegerField, Sum
from django.db import models
import pandas as pd
from rest_framework.views import APIView 
from rest_framework.response import Response
# from django.core.mail import send_mail
import os
# from io import BytesIO #A stream implementation using an in-memory bytes buffer
# # It inherits BufferIOBase
from django.template.loader import render_to_string, get_template
# #pisa is a html2pdf converter using the ReportLab Toolkit,
# #the HTML5lib and pyPdf.
from xhtml2pdf import pisa  
#difine render_to_pdf() function
#import render_to_pdf from util.py 
#Creating our view, it is a class based view
import pdfkit 
from rest_framework.renderers import BaseRenderer
# from puppeteer_pdf import render_pdf_from_template
# from puppeteer_pdf.views import PDFResponse
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
# import reportlab
# from reportlab.pdfgen import canvas
from django.http import FileResponse
import json
import numpy as np
from FinalProject.settings import EMAIL_HOST_USER
# from . import forms
from django.core.mail import send_mail , EmailMessage


# config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
def render_to_pdf(request,Teacher_Name, media_type=None, renderer_context=None):
    # content start
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
  
    # Creating Graphs for pdf
    #Regular and punctual graph
    fig1 = plt.barh(Regular_Punctual_unique, Regular_Punctual_data, align = 'center')
    plt.tight_layout()
    buffer1 = BytesIO()
    plt.savefig(buffer1, format='png')
    buffer1.seek(0)
    image_png1 = buffer1.getvalue()
    buffer1.close()
    graphic1 = base64.b64encode(image_png1).decode('utf-8')
    plt.close()
    # Knowledge 
    fig2 = plt.barh(Knowledge_unique, Knowledge_data, align = 'center')
    plt.tight_layout()
    buffer2 = BytesIO()
    plt.savefig(buffer2, format='png')
    buffer2.seek(0)
    image_png2 = buffer2.getvalue()
    buffer2.close()
    graphic2 = base64.b64encode(image_png2).decode('utf-8')
    plt.close()
    #clarity
    fig3 = plt.barh(Clarity_communication_unique, Clarity_communication_data, align = 'center')
    plt.tight_layout()
    buffer3 = BytesIO()
    plt.savefig(buffer3, format='png')
    buffer3.seek(0)
    image_png3 = buffer3.getvalue()
    buffer3.close()
    graphic3 = base64.b64encode(image_png3).decode('utf-8')
    plt.close()
    # help student
    fig4 = plt.barh(helpStudent_unique, helpStudent_data, align = 'center')
    plt.tight_layout()
    buffer4 = BytesIO()
    plt.savefig(buffer4, format='png')
    buffer4.seek(0)
    image_png4 = buffer4.getvalue()
    buffer4.close()
    graphic4 = base64.b64encode(image_png4).decode('utf-8')
    plt.close()
    #presentation
    fig5 = plt.barh(presentation_unique, presentation_data, align = 'center')
    plt.tight_layout()
    buffer5 = BytesIO()
    plt.savefig(buffer5, format='png')
    buffer5.seek(0)
    image_png5 = buffer5.getvalue()
    buffer5.close()
    graphic5 = base64.b64encode(image_png5).decode('utf-8')
    plt.close()
    # motivate interest
    fig6 = plt.barh(motivatesInterest_unique, motivatesInterest_data, align = 'center')
    plt.tight_layout()
    buffer6 = BytesIO()
    plt.savefig(buffer6, format='png')
    buffer6.seek(0)
    image_png6 = buffer6.getvalue()
    buffer6.close()
    graphic6 = base64.b64encode(image_png6).decode('utf-8')
    plt.close()
    # co-operative
    fig7 = plt.barh(co_opeartive_unique, co_opeartive_data, align = 'center')
    plt.tight_layout()
    buffer7 = BytesIO()
    plt.savefig(buffer7, format='png')
    buffer7.seek(0)
    image_png7 = buffer7.getvalue()
    buffer7.close()
    graphic7 = base64.b64encode(image_png7).decode('utf-8')
    plt.close()
    # new outlook
    fig8 = plt.barh(newOutlook_unique, newOutlook_data, align = 'center')
    plt.tight_layout()
    buffer8 = BytesIO()
    plt.savefig(buffer8, format='png')
    buffer8.seek(0)
    image_png8 = buffer8.getvalue()
    buffer8.close()
    graphic8 = base64.b64encode(image_png8).decode('utf-8')
    plt.close()
    #9 Checking
    fig9 = plt.barh(checking_unique, checking_data, align = 'center')
    plt.tight_layout()
    buffer9 = BytesIO()
    plt.savefig(buffer9, format='png')
    buffer9.seek(0)
    image_png9 = buffer9.getvalue()
    buffer9.close()
    graphic9 = base64.b64encode(image_png9).decode('utf-8')
    plt.close()
    # seminar
    fig10 = plt.barh(seminar_unique, seminar_data, align = 'center')
    plt.tight_layout()
    buffer10 = BytesIO()
    plt.savefig(buffer10, format='png')
    buffer10.seek(0)
    image_png10 = buffer10.getvalue()
    buffer10.close()
    graphic10 = base64.b64encode(image_png10).decode('utf-8')
    plt.close()
    # interection
    fig11 = plt.barh(interaction_unique, interaction_data, align = 'center')
    plt.tight_layout()
    buffer11 = BytesIO()
    plt.savefig(buffer11, format='png')
    buffer11.seek(0)
    image_png11 = buffer11.getvalue()
    buffer11.close()
    graphic11 = base64.b64encode(image_png11).decode('utf-8')
    plt.close()
    # effectivness
    fig12 = plt.barh(effectiveness_unique, effectiveness_data, align = 'center')
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
    # Contents ends
#     #  pdf = render_pdf_from_template(
#     #         input_template='TeacherFeedbackReport.html',
#     #         header_template='',
#     #         footer_template='',
#     #         context=context,
#     #         cmd_options={
#     #             'format': 'A3',
#     #             'scale': '0.9',
#     #             'landscape': True,
#     #             'displayHeaderFooter': False,
#     #             'marginTop': '90px',
#     #             'marginLeft': '50px',
#     #             'marginRight': '50px',
#     #             'marginBottom': '50px',
#     #         }
#     #  )
#     #  return PDFResponse(pdf)

    
    
#      #This part will create the pdf.
    


# working
    media_type = 'application/pdf'
    format = 'pdf'
    charset = 'utf-8'
    template = get_template('TeacherFeedbackReportpdf.html')
    html  = template.render(context)
    result = BytesIO()
#      #This part will create the pdf.
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    # if not pdf.err:
    #     response = HttpResponse(result.getvalue())
    #     response['Content-Disposition'] = 'filename="invoicex.pdf"'
    #     subject = 'Your Monthly feedback'
        # message = 'Here is your feed back for the month of ...........'
        # recepient = 'kaxyapdip@gmail.com'
        # send_mail =EmailMessage (subject, 
        # message, EMAIL_HOST_USER, [recepient])
        # send_mail.attach('invoicex.pdf', result.getvalue() , 'application/pdf')
        # send_mail.send()
        # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        # return HttpResponse(result.getvalue(), content_type='application/pdf')
    # return render(request, 'success.html', {'recepient': recepient})
    return HttpResponse(result.getvalue(), content_type='application/pdf')
    # html_string = context
    # html = HTML(string=html_string)
    # result = html.write_pdf()

    # # Creating http response
    # response = HttpResponse(content_type='application/pdf;')
    # response['Content-Disposition'] = 'inline; filename=list_people.pdf'
    # response['Content-Transfer-Encoding'] = 'binary'
    # with tempfile.NamedTemporaryFile(delete=True) as output:
    #     output.write(result)
    #     output.flush()
    #     output = open(output.name, 'r')
    #     response.write(output.read())

    # return response


#     options = {
#         'page-size': 'A4',
#         'margin-top': '0.55in',
#         'margin-right': '0.55in',
#         'margin-bottom': '0.55in',
#         'margin-left': '0.55in',
#         'encoding': "UTF-8",
#         # any other wkhtmltopdf options
#         }
#     pdf = pdfkit.PDFKit(context, "string", options=options, configuration=config).to_pdf()
#     response = HttpResponse(pdf)
#     response['Content-Type'] = 'application/pdf'
#          # change attachment to inline if you want open file in browser tab instead downloading
#     response['Content-disposition'] = 'inline;filename={}.pdf'.format('my pdf')
#     return response 
# def render_to_pdf(request):
#     from reportlab.lib import colors
#     from reportlab.graphics.shapes import Drawing
#     from reportlab.graphics.charts.barcharts import HorizontalBarChart
#     # Create a file-like buffer to receive PDF data.
#     buffer = io.BytesIO()
#     # Create the PDF object, using the buffer as its "file."
#     p = canvas.Canvas(buffer)
#     # Draw things on the PDF. Here's where the PDF generation happens.
#     # See the ReportLab documentation for the full list of functionality.
#     p.drawString(100, 100, "Hello world.")
#     # Close the PDF object cleanly, and we're done.
#     p.showPage()
#     p.save()
#     # FileResponse sets the Content-Disposition header so that browsers
#     # present the option to save the file.
#     buffer.seek(0)
#     drawing = Drawing(400, 200)
#     data = [
#            (13, 5, 20, 22, 37, 98, 19, 4),
#            ]
#     names = ["Cat %s" % i for i in range(1, len(data[0])+1)]
#     bc = HorizontalBarChart()
#     bc.x = 20
#     bc.y = 50
#     bc.height = 200
#     bc.width = 400
#     bc.data = data
#     bc.strokeColor = colors.white
#     bc.valueAxis.valueMin = 0
#     bc.valueAxis.valueMax = 100
#     bc.valueAxis.valueStep = 10
#     bc.categoryAxis.labels.boxAnchor = 'ne'
#     bc.categoryAxis.labels.dx = -10
#     bc.categoryAxis.labels.fontName = 'Helvetica'
#     bc.categoryAxis.categoryNames = names
#     drawing.add(bc)
#     return drawing
#     return FileResponse(buffer, as_attachment=True, filename='hello.pdf') 
#  //report lab
# from reportlab.platypus import SimpleDocTemplate, Paragraph, Table , TableStyle, Image
# from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
# from reportlab.lib.enums import TA_CENTER
# from django.contrib.auth.models import User
# from reportlab.lib.pagesizes import A4
# import datetime as date
# from reportlab.graphics.shapes import Drawing    
# from reportlab.graphics.charts.barcharts import VerticalBarChart
# from reportlab.lib import colors
# fileName = 'pdfTable.pdf'
# from reportlab.lib.pagesizes import letter
# pdf = SimpleDocTemplate(fileName,pagesize=letter)
# from reportlab.graphics.shapes import Drawing
# from reportlab.lib import colors
# from reportlab.platypus import Table
# from reportlab.graphics.shapes import String
# from reportlab.graphics.charts.barcharts import HorizontalBarChart
# def getVerticalBarChart():
# 	data = [
# 		(3, 18, 20),
# 		(14, 12, 21)
# 	]  
# 	chart = VerticalBarChart()
# 	chart.data = data
# 	chart.valueAxis.valueMin = 0
# 	chart.valueAxis.valueMax = 25
# 	chart.valueAxis.valueStep = 5
# 	chart.x = 5
# 	chart.y = 5
# 	chart.height = 100
# 	chart.width = 240
# 	chart.strokeColor = colors.black
# 	chart.fillColor = colors.yellow
# 	chart.groupSpacing = 0
# 	chart.categoryAxis.categoryNames = [
# 		'A','B','C'
# 	]
# 	title = String(
# 		50, 110,
# 		'Vertical Bar Chart',
# 		fontSize = 14
# 	)
# 	drawing = Drawing(240, 120)
# 	drawing.add(title)
# 	drawing.add(chart)
# 	return drawing
# def render_to_pdf(request):
#     response = HttpResponse(content_type='application/pdf')
#     subTitle = 'hello Groot'
#     filename = 'pdf_demo'
#     response['Content-Disposition'] = 'inline; filename={0}.pdf'.format(filename)
#     buffer = io.BytesIO()
#     c = canvas.Canvas(buffer, pagesize=A4)
#     d = Drawing(width=400, height=200)
#     #header
#     c.setLineWidth(.3)
#     c.setFont('Helvetica', 22)
#     c.drawString(30,750,'hello')
#     c.setFont('Helvetica', 22)
#     c.drawString(30,770,'groot') 
#     c.line(450, 747, 560,747)
#     # c.showPage()
#     c.drawCentredString(290,720, subTitle)
#     data = [
#            (13, 5, 20, 22, 37, 98, 19, 4),
#            ]
#     names = ["Cat %s" % i for i in range(1, len(data[0])+1)]
#     bc = HorizontalBarChart()
#     bc.x = 20
#     bc.y = 50
#     bc.height = 200
#     bc.width = 400
#     bc.data = data
#     bc.strokeColor = colors.white
#     bc.valueAxis.valueMin = 0
#     bc.valueAxis.valueMax = 100
#     bc.valueAxis.valueStep = 10
#     bc.categoryAxis.labels.boxAnchor = 'ne'
#     bc.categoryAxis.labels.dx = -10
#     bc.categoryAxis.labels.fontName = 'Helvetica'
#     bc.categoryAxis.categoryNames = names
#     d.add(bc)
#     d.drawOn(c,0,0)
# 	d.save(formats=['pdf'])    
# 	pdf = buffer.getvalue()
#     buffer.close()
#     response.write(pdf)
#     return response



def sent_mail(request):
    subject = 'Monthly feedback'
    message = 'Hope you are enjoying your Teaching'
    recepient = 'kaxyapdip@gmail.com'
    send_mail(subject, 
    message, EMAIL_HOST_USER, [recepient], fail_silently = False)
    return render(request, 'success.html', {'recepient': recepient})

    