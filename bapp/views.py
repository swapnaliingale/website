from django.shortcuts import render
from bapp.models import project,fclient
from.forms import enquiryform

# Create your views here.
def index(request):
    return render(request,'bapp/index.html')

def service(request):
    data=project.objects.all
    return render(request,'bapp/service.html',{'data':data})

def client(request):
    i_data=fclient.objects.all
    return render(request,'bapp/client.html',{'i_data':i_data})

def enquiry(request):
    if request.method=='POST':
        form=enquiryform(request.POST)
        if form.is_valid():
            form.save()

    form=enquiryform()
    return render(request,'bapp/enquiry.html',{'form':form})