from django.shortcuts import render
from .models import Dl

# Create your views here.

def home(request):
    dls=Dl.objects.all()
    params={"dls":dls}
    return render(request,"main/home.html")

def dl(request,dl):
    dlobj=Dl.objects.get(name=dl)
    return render(request,dlobj.file)

