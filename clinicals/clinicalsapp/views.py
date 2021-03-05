from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from clinicalsapp.forms import ClinicalDataForm
from clinicalsapp.models import Patient, ClinicalData
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


# Create your views here.

class PatientListView(ListView):
    model = Patient


class PatientCreateView(CreateView):
    model = Patient
    success_url = reverse_lazy('patient_list')
    fields = ('first_name', 'last_name', 'age')


class PatientUpdateView(UpdateView):
    model = Patient
    success_url = reverse_lazy('patient_list')
    fields = ('first_name', 'last_name', 'age')


class PatientDeleteView(DeleteView):
    model = Patient
    success_url = reverse_lazy('patient_list')


def add_data(request, **kwargs):
    form = ClinicalDataForm()
    patient = Patient.objects.get(pk=kwargs['pk'])
    if request.method == 'POST':
        form = ClinicalDataForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('patient_list')
    return render(request, 'clinicalsapp/add_data.html', {'form':form, 'patient':patient})


def analyze(request, **kwargs):
    data = ClinicalData.objects.filter(patient_id=kwargs['pk'])
    response_data = []
    for each_entry in data:
        if each_entry.component_name == 'hw':
            height_and_weight = each_entry.component_value.split('/')
            if len(height_and_weight) > 1:
                feet_to_meters = float(height_and_weight[0]) * 0.4536
                BMI = (float(height_and_weight[1])) / (feet_to_meters ** 2)
                bmi_entry = ClinicalData()
                bmi_entry.component_name = 'BMI'
                bmi_entry.component_value = BMI
                response_data.append(bmi_entry)
        response_data.append(each_entry)

    return render(request, 'clinicalsapp/generate_report.html', {'data':response_data})