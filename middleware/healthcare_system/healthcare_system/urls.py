"""
URL configuration for healthcare_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from healthcare_system_django.views import signup, login, get_hospital_details, get_doctor_availability

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup),
    path('login/', login),
    path('gethospitalsdetails/', get_hospital_details),
    path('get-doctor-availability/', get_doctor_availability)
]
