from django import forms
from .models import CityModel, SchoolModel, StudentModel

class CityForm(forms.ModelForm):
    class Meta:
        model = CityModel
        fields = '__all__'

class SchoolForm(forms.ModelForm):
    class Meta:
        model = SchoolModel
        fields = '__all__'

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'