from django import forms
from . models import Customer, Province, City

class CustomerForm(forms.ModelForm):
    class Meta:
        model= Customer
        fields= ['lastname', 'firstname', 'middlename', 'birthday', 'homeaddress', 'homeownership', 'phone', 'businessname', 'specialtypractice', 'tenurepractice', 'prcno', 'businessaddress', 'businessphone', 'businessemail', 'contactperson', 'position', 'contactpersonphone', 'image1', 'image2', 'businesstype', 'region', 'province', 'city']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['province'].queryset = Province.objects.none()



        if 'region' in self.data:
            try:
                region_id = int(self.data.get('region'))
                self.fields['province'].queryset = Province.objects.filter(region_id=region_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['province'].queryset = self.instance.region.province_set.order_by('name')

        self.fields['city'].queryset = Province.objects.none()
        if 'province' in self.data:
            try:
                province_id = int(self.data.get('province'))
                self.fields['city'].queryset = City.objects.filter(province_id=province_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.region.province.city_set.order_by('name')
