from django.shortcuts import render
from .models import Teacher_Register , Teacher_signUp
from .resources import Teacher_RegisterResource , Teacher_signUpResource 
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse , HttpResponseRedirect
# Create your views here.
def teacher_upload(request):
    if request.method == 'POST':
       
        teacher_RegisterResource = Teacher_RegisterResource()
        dataset = Dataset()
        new_tRegister = request.FILES['myfile']

        if not new_tRegister.name.endswith('xlsx'):
            messages.info(request,'wrong format')
            return render(request,'upload.html',{'title': 'Teacher Regisstration'})
        imported_data = dataset.load(new_tRegister.read(),format='xlsx')
        for data in imported_data:
            value = Teacher_Register(
                data[0],
                data[1],
                data[2],
                data[3],
                'Pending'
                 )
            value.save()
            
        messages.info(request,'Records Inserted')
        generate_users(request)
        # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request,'upload.html',{'title': 'Teacher data Upload'})

def generate_users(request):
    
    context = Teacher_Register.objects.all()
    # print(context)
    for data in context:
        value = Teacher_signUp(
                UserName = data.Teacher_Name,
                Password = data.Mobile,
                Role = 'user'

                )
        value.save()
    messages.info(request,'Teacher login Credentials is generated')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


