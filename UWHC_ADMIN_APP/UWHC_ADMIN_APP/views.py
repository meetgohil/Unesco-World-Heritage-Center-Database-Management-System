#views.py
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages 
from django.http import HttpResponse
from UWHC_ADMIN_APP.models import SiteModel
from UWHC_ADMIN_APP.forms import SiteForms
from UWHC_ADMIN_APP.models import InstModel
from UWHC_ADMIN_APP.forms import InstForms
from UWHC_ADMIN_APP.models import CountryModel
from UWHC_ADMIN_APP.forms import CountryForms

def homepage(request):
    return render(request, 'index.html')

def search_site(request):
    q = request.POST.getlist('query')
    if 'Natural' in q:
        sites=SiteModel.objects.filter(category__contains='Natural')
    elif 'Cultural' in q:
        sites=SiteModel.objects.filter(category__contains='Cultural')
    elif 'Mixed' in q:
        sites=SiteModel.objects.filter(category__contains='Mixed')
    elif 'Outstanding Universal Value' in q:
        sites=SiteModel.objects.filter(category__contains='Outstanding Universal Value')
    else:
        sites=SiteModel.objects.all()
    context = {"data":sites}
    return render(request, 'index.html', context)

def adminlogin(request):
    return render(request, 'adminun.html')

def login(request):
    return render(request, 'login.html')

def showinst(request):
    showall=InstModel.objects.all()
    return render(request,'institute.html',{"data":showall})

def insertinst(request):
    if request.method=='POST':
        if request.POST.get('institute_id') and request.POST.get('institute_name') and request.POST.get('officer') and request.POST.get('address') and request.POST.get('contact'):
            saverecord=InstModel()
            saverecord.institute_id=request.POST.get('institute_id')
            saverecord.institute_name=request.POST.get('institute_name')
            saverecord.officer=request.POST.get('officer')
            saverecord.address=request.POST.get('address')
            saverecord.contact=request.POST.get('contact')
            saverecord.save()
            messages.success(request,'Institute "'+saverecord.institute_name+ '" is saved successfully.!' )
            return render(request, 'insertinst.html')
    else:
        return render(request, 'insertinst.html')
        
def editinst(request, institute_id):
    editempobj=InstModel.objects.get(institute_id=institute_id)
    return render(request, 'editinst.html', {"InstModel":editempobj})

def updateinst(request, institute_id):
    updateemp=InstModel.objects.get(institute_id=institute_id)
    form=InstForms(request.POST, instance=updateemp)
    if form.is_valid():
        form.save()
        messages.success(request, "Record Updated Successfully...!")
        return render(request, 'editinst.html', {"InstModel":updateemp})

def delinst(request, institute_id):
    Delemp=InstModel.objects.get(institute_id=institute_id)
    Delemp.delete()
    #showdata=InstModel.objects.all()
    return redirect('showinst')


def showsite(request):
    showall=SiteModel.objects.all()
    return render(request,'site.html',{"data":showall})

def insertsite(request):
    if request.method=='POST':
        if request.POST.get('s_id') and request.POST.get('site_name') or request.POST.get('address') or request.POST.get('latitude') or request.POST.get('longitude') or request.POST.get('area') or request.POST.get('country_code') or request.POST.get('category') or request.POST.get('buffer_zone') or request.POST.get('historical_detail') or request.POST.get('ownership') or request.POST.get('institute_id'):
            saverecord=SiteModel()
            saverecord.s_id=request.POST.get('s_id')
            saverecord.site_name = request.POST.get('site_name')
            saverecord.address=request.POST.get('address')
            saverecord.latitude=request.POST.get('latitude')
            saverecord.longitude=request.POST.get('longitude')
            saverecord.area=request.POST.get('area')
            saverecord.country_code=request.POST.get('country_code')
            saverecord.category=request.POST.get('category')
            saverecord.buffer_zone=request.POST.get('buffer_zone')
            saverecord.historical_detail=request.POST.get('historical_detail')
            saverecord.ownership=request.POST.get('ownership')
            saverecord.institute_id=request.POST.get('institute_id')
            saverecord.save()
            messages.success(request,'Site "' +saverecord.site_name+'" is saved successfully.!' )
    return render(request, 'insertsite.html')

def editsite(request, s_id):
    editempobj=SiteModel.objects.get(s_id=s_id)
    return render(request, 'editsite.html', {"SiteModel":editempobj})

def updatesite(request, s_id):
    updatest=SiteModel.objects.get(s_id=s_id)
    form=SiteForms(request.POST, instance=updatest)
    if form.is_valid():
        form.save()
        messages.success(request, "Record Updated Successfully...!")
        return render(request, 'editsite.html', {"SiteModel":updatest})

def delsite(request, s_id):
    Delemp=SiteModel.objects.get(s_id=s_id)
    Delemp.delete()
    #showdata=InstModel.objects.all()
    return redirect('showsite')


def showcountry(request):
    showall=CountryModel.objects.all()
    return render(request,'country.html',{"data":showall})

def insertcountry(request):
    if request.method=='POST':
        if request.POST.get('country_code') and request.POST.get('country_name') and request.POST.get('donor_id') and request.POST.get('region') and request.POST.get('veto_power')and request.POST.get('representative'):
            saverecord=CountryModel()
            saverecord.country_code=request.POST.get('country_code')
            saverecord.country_name=request.POST.get('country_name')
            saverecord.donor_id=request.POST.get('donor_id')
            saverecord.region=request.POST.get('region')
            saverecord.veto_power=request.POST.get('veto_power')
            saverecord.representative=request.POST.get('representative')
            saverecord.save()
            messages.success(request,'Country "'+saverecord.country_name+'" is saved successfully.!' )
            return render(request, 'insertcountry.html')
    else:
        return render(request, 'insertcountry.html')
        
def editcountry(request, country_code):
    editempobj=CountryModel.objects.get(country_code=country_code)
    return render(request, 'editcountry.html', {"CountryModel":editempobj})

def updatecountry(request, country_code):
    updateemp=CountryModel.objects.get(country_code=country_code)
    form=CountryForms(request.POST, instance=updateemp)
    if form.is_valid():
        form.save()
        messages.success(request, "Record Updated Successfully...!")
        return render(request, 'editcountry.html', {"CountryModel":updateemp})

def delcountry(request, country_code):
    Delemp=CountryModel.objects.get(country_code=country_code)
    Delemp.delete()
    #showdata=InstModel.objects.all()
    return redirect('showcountry')
