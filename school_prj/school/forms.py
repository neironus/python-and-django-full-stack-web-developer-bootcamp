from django import forms
from django.forms import ModelForm, Textarea, TextInput
from django.forms.widgets import Select
from .models import CityModel, SchoolModel, StudentModel


class CityForm(forms.ModelForm):
    class Meta:
        model = CityModel
        fields = '__all__'


class SchoolForm(forms.ModelForm):
    def clean_name(self, *args, **kwargs):
        name = self.cleaned_data.get('name')
        if '@' in name:
            raise forms.ValidationError("В имени школы не должны присутствовать символ - @")
        else:
            return name

    class Meta:
        model = SchoolModel
        fields =  ('name', 'slug')
        labels = {
            'name': 'Название школы',
            'slug': 'URL школы'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'bg-primary display-4'}),
            'slug': forms.TextInput(attrs={'class': 'bg-danger display-4'})
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
