from django.shortcuts import render
from .models import Teacher_Feedback
from .resources import Teacher_FeedbackResource 
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse , HttpResponseRedirect
# Create your views here.
def simple_upload(request):
    if request.method == 'POST':
        teacher_FeedbackResource = Teacher_FeedbackResource()
        dataset = Dataset()
        new_Feedback = request.FILES['myfile']

        if not new_Feedback.name.endswith('xlsx'):
            messages.info(request,'wrong format')
            return render(request,'upload.html',{'title': 'Feedback Upload'})
        imported_data = dataset.load(new_Feedback.read(),format='xlsx')
        for data in imported_data:
            value = Teacher_Feedback(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
                data[8],
                data[9],
                data[10],
                data[11],
                data[12],
                data[13],
                data[14],
                data[15],
                data[16],
                data[17],
                data[18],
                data[19],
                data[20],
                data[21],
                
                    )
            value.save()
        messages.info(request,'Records Inserted')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))  
        
    return render(request,'upload.html',{'title': 'Feedback Upload'})