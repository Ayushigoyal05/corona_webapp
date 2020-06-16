from django.shortcuts import render
from django.views import generic
from .models import Ventilator, Hospital, Bed, Patient


def graphic(request):
    pat=Patient.objects.all().last()
    hos=Hospital.objects.all().last()
    bd=Bed.objects.all().last()
    ven=Ventilator.objects.all().last()
    # print(pat)
    # print(total)
    # print(pat.recovered)
    context={'pat':pat,'hos':hos,'bd':bd,'ven':ven}
    return render(request,'graphical.html',context)

def ventilators(request):
    venti=Ventilator.objects.all()
    return render(request,'ventilators.html',{'venti':venti})

def hospitals(request):
    hosp=Hospital.objects.all()
    return render(request, 'hospitals.html',{'hosp':hosp})

def beds(request):
    bed=Bed.objects.all()
    return render(request, 'beds.html',{'bed':bed})

def home(request):
    pat2=Patient.objects.all()
    return render(request,'home.html',{'pat2':pat2})


    



# Create your views here.
