from django.core import validators
from django import forms
from .models import * 

class StudentRegistrations(forms.ModelForm):
    class Meta:
        model = Register
        fields =['Name', 'Email', 'Password']
        widgets = {
            'Name': forms.TextInput(attrs={'class':'form-control'}),
            'Email': forms.EmailInput(attrs={'class':'form-control'}),
            'Password': forms.PasswordInput(render_value=True, attrs={'class':'form-control'})
        }
    def clean(self):
        super(StudentRegistrations, self).clean()

        Name = self.cleaned_data.get('Name')
        Email = self.cleaned_data.get('Email')
        Password = self.cleaned_data.get('Password')

        if len(Name) < 7:
            self._errors['Name'] = self.error_class(['A minimum 7 character required...'])

        if len(Password) < 8:
            self._errors['Password'] = self.error_class(['Password length should not be less than 8 characters'])
        
        return self.cleaned_data

class StudentLogin(forms.Form):
    class Meta:
        model = Register
        fields = ['Email','Password']
        