from django.forms import ModelForm
from teacher_Register.models import Teacher_signUp

class Teacher_signUpFields(ModelForm):
    class Meta:
        model = Teacher_signUp
        fields = '__all__'