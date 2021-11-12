from django import forms
from django.db.models import fields
from django.forms import widgets
from django.contrib.auth.forms import AuthenticationForm
from .models import *

class AddParametersForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['engine'].empty_label = 'Двигатель не выбран'
        self.fields['station'].empty_label = 'Станция не выбрана'

    class Meta:
        model = Parameters
        fields = ['OT_in_day', 'max_power', 'max_temperature', 'duty_officer', 'volume_oil',
                'journal', 'time_work', 'photo', 'status', 'TO', 'engine', 'station']
        widgets = {
            'OT_in_day': forms.TextInput(attrs={'class':'form-control'}),
            'journal': forms.Textarea(attrs={'rows': 4, 'cols':60, 'class':'form-control'}),
            'max_power': forms.TextInput(attrs={'class':'form-control'}),
            'max_temperature': forms.TextInput(attrs={'class':'form-control'}),
            'duty_officer': forms.TextInput(attrs={'class':'form-control'}),
            'volume_oil': forms.TextInput(attrs={'class':'form-control'}),
            'status': forms.TextInput(attrs={'class':'form-control'}),
            'time_work': forms.TextInput(attrs={'type':'datetime-local', 'class':'form-control'}),
            'engine': forms.Select(attrs={'class':'form-control'}),
            'station': forms.Select(attrs={'class': 'form-control'}),
        }

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'input100', 'name':'email' ,'type': 'text', 'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label='Пароль', widget=forms.TextInput(attrs={'class': 'input100', 'name':'pass' ,'type': 'password', 'placeholder': 'Пароль'}))        