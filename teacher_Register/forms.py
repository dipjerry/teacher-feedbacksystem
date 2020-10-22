from django.forms import ModelForm
from .models import Teacher_Register

class TeacherRegisterFields(ModelForm):
    class Meta:
        model = Teacher_Register
        fields = ['Email', 'Mobile']

         

   
    