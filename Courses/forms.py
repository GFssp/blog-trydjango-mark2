from django.forms import ModelForm
from .models import CourseModel
from django.forms import forms

class CourseModelForm(ModelForm):
    class Meta:
        model = CourseModel
        fields = [
            'title',
        ]

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title.lower() == "abc":
            raise forms.ValidationError("Not valid form title")