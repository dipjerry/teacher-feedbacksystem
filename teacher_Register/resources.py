from import_export import resources
from .models import Teacher_Register, Teacher_signUp
class Teacher_RegisterResource(resources.ModelResource):
    class meta:
        model = Teacher_Register
class Teacher_signUpResource(resources.ModelResource):
    class meta:
        model = Teacher_signUp
