from django import forms


class FeedbackForm(forms.Form):
    tName = forms.CharField(label = "Teacher Name", max_length = 100),
    remark = forms.CharField(label = "remark", max_length = 100)