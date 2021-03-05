"""clinicals URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from clinicalsapp.views import PatientListView, PatientCreateView, PatientUpdateView, PatientDeleteView, add_data, \
    analyze

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PatientListView.as_view(), name='patient_list'),
    path('patient_create', PatientCreateView.as_view(), name='patient_create'),
    path('patient_update/<int:pk>/', PatientUpdateView.as_view(), name='patient_update'),
    path('patient_delete/<int:pk>/', PatientDeleteView.as_view(), name='patient_delete'),
    path('add_data/<int:pk>/', add_data, name='add_data'),
    path('analyze/<int:pk>/', analyze, name='analyze')

]
