from django import forms
from mainApp.models import *
from bootstrap_modal_forms.forms import BSModalForm
from db_file_storage.form_widgets import DBAdminClearableFileInput
from db_file_storage.form_widgets import DBClearableFileInput
from django.contrib import admin

class CustomizeOrderForm(forms.ModelForm):
    Name=forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'type':'text',
            'style':'height: 52px; width: 100%;background-color: #f3f5f8;margin-bottom: 15px;border: none;',
            'placeholder':'Name'
        }
    ))
    Email=forms.CharField(widget=forms.EmailInput(
        attrs={
            'class':'form-control',
            'type':'email',
            'placeholder':'Email',
            'style':'height: 52px; width: 100%;background-color: #f3f5f8;margin-bottom: 15px;border: none;',
        }
    ))
    Phone=forms.CharField(widget=forms.NumberInput(
        attrs={
            'class':'form-control',
            'type':'tel',
            'style':'height: 52px; width: 100%;background-color: #f3f5f8;margin-bottom: 15px;border: none;',
            'placeholder':'Phone'
        }
    ))
    Details=forms.CharField(widget=forms.Textarea(
        attrs={
            'class':'form-control',
            'type':'text',
            'style':'height: 100px; width: 100%;background-color: #f3f5f8;margin-bottom: 15px;border: none;',
            'placeholder':'Tell us a bit about your requirements'
        }
    ))
    class Meta():
        model=CustomizeOrderTable
        fields=('Name','Email','Phone','Details')
        