"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from webapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('',index,name="index"),
    path('blog/',blog,name="blog"),
    path('adminview/',adminview,name="adminview"),
    path('result/',result,name="result"),
    path('chatbot/',chatbot,name="chatbot"),
    path('faq/',faq,name="faq"),
    path('MHstatusPAST_view/', MHstatusPAST_view,name='MHstatusPAST_view'),
    path('MHstatusNOW_view/', MHstatusNOW_view,name='MHstatusNOW_view'),
    path('country_view/', country_view, name='country_view'),
    path('gender_view/', gender_view,name='gender_view'),

]
