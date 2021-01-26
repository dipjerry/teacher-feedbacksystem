from import_export import resources
from .models import Teacher_Feedback
class Teacher_FeedbackResource(resources.ModelResource):
    class meta:
        model = Teacher_Feedback
