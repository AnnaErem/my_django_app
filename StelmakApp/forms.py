# from django.forms import ModelForm
from django import forms
from django.forms import ModelForm
from .models import Educational_ProgrammModel


class ProgrammForm(forms.Form):
    name = forms.CharField(initial = "Иван Иванович Иванов")
    date_of_birth = forms.IntegerField(initial=2005, min_value=1950) #здесь можно изменить формат на дату
    year = forms.IntegerField(initial=2023,required=False)
    courses = forms.IntegerField(initial=1)
    last_year = forms.IntegerField(initial=2027)



class Educational_ProgrammModelFrom(ModelForm):
    # task = forms.CharField(widget=forms.Textarea({'cols': '60', 'rows': "3"}))
    # task.widget.attrs.update({'cols': '40', 'rows': "2"})
    class Meta:
        model = Educational_ProgrammModel
        fields = '__all__'
        # fields = ['task', 'a', 'b','c']
        print('\nfields: ', fields)