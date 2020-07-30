from django import forms
from . models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model= Customer
        fields= ['lastname', 'firstname', 'middlename', 'birthday', 'homeaddress', 'homeownership', 'phone', 'businessname', 'specialtypractice', 'tenurepractice', 'prcno', 'businessaddress', 'businessphone', 'businessemail', 'contactperson', 'position', 'contactpersonphone']
        
