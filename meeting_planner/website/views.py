# from django.shortcuts import render
from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

from meetings.models import Meeting


def welcome(request):
     return render(request, "website/welcome.html", 
         {"meetings": Meeting.objects.all()}  # template context
     )

def date(request):
    return HttpResponse("this page was served at" +str(datetime.now()))

def about(request):
    return HttpResponse("My name is Sumit Kumar Pandey and i learn django in Pluralsight")


# Create your views here.
