#urls.py
"""UWHC-Admin-App URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic import RedirectView
from django.conf.urls import url
from django.shortcuts import render
from django.views.static import serve
from django.contrib.staticfiles.storage import staticfiles_storage

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('adminun', views.adminlogin, name="adminlogin"),
    path('login', views.login, name="login"),
    path('search_site', views.search_site, name="search-site"),
    
    path('institute',views.showinst, name="showinst"),
    path('insert', views.insertinst, name="insertinst"),
    path('edit/<int:institute_id>',views.editinst,name="editinst"),
    path('update/<int:institute_id>', views.updateinst, name="updateinst"),
    path('delete/<int:institute_id>', views.delinst, name="delinst"),

    path('site',views.showsite, name="showsite"),
    path('inserts', views.insertsite, name="insertsite"),
    path('edits/<int:s_id>',views.editsite,name="editsite"),
    path('updates/<int:s_id>', views.updatesite, name="updatesite"),
    path('deletes/<int:s_id>', views.delsite, name="delsite"),

    path('country',views.showcountry, name="showcountry"),
    path('insertcnt', views.insertcountry, name="insertcountry"),
    path('editcnt/<int:country_code>',views.editcountry,name="editcountry"),
    path('updatecnt/<int:country_code>', views.updatecountry, name="updatecountry"),
    path('deletecnt/<int:country_code>', views.delcountry, name="delcountry"),

    path('admin/', admin.site.urls),
    
    # url(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),
    path('unesco_logo.png', RedirectView.as_view(url=staticfiles_storage.url('images/unesco_logo.png'))),
]


