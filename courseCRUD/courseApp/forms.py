from django import forms
from .import models

class courseForm(forms.ModelForm):
    class Meta:
        model = models.Course
        fields = '__all__'
