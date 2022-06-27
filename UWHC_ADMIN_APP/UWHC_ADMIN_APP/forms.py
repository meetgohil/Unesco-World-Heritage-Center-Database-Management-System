#forms.py
from django import forms
from UWHC_ADMIN_APP.models import InstModel
from UWHC_ADMIN_APP.models import SiteModel
from UWHC_ADMIN_APP.models import CountryModel

class InstForms(forms.ModelForm):
    class Meta: 
        model=InstModel
        fields="__all__"

class SiteForms(forms.ModelForm):
    class Meta: 
        model=SiteModel
        fields="__all__"

class CountryForms(forms.ModelForm):
    class Meta: 
        model=CountryModel
        fields="__all__"

