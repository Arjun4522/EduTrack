from django import forms
from django.contrib.auth.models import User
#from .models import AdditionalInfo


class RegistrationForm(forms.Form):
    enrollment_number = forms.CharField(label='Enrollment Number',min_length=10,max_length=10)
    first_name = forms.CharField(label='First Name',max_length=30)
    last_name = forms.CharField(label='Last Name',max_length=30)
    email = forms.EmailField(label='Email',max_length=75)
    phone_number = forms.CharField(label='Phone',max_length=15)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['enrollment_number', 'first_name', 'last_name', 'email', 'phone_number', 'password']


#class AdditionalInfoForm(forms.ModelForm):
#   class Meta:
#        model = AdditionalInfo
#        fields = ['date_of_birth', 'address', 'guardian_name', 'class_10_marks', 'class_12_marks']
