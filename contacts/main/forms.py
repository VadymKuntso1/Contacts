from .models import Contact
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','seccond_name','third_name',
                  'number','photo']
        widgets = {
            'name':forms.TextInput(attrs={'class' : 'form-control'}),
            'seccond_name': forms.TextInput(attrs={'class' : 'form-control'}),
            'third_name': forms.TextInput(attrs={'class' : 'form-control'}),
            'number': forms.TextInput(attrs={'class' : 'form-control'}),
            'photo': forms.FileInput()
        }