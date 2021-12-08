# from django.shortcuts import render
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):
    return render(request, "website/welcome.html",
                {"message":"this data was sent from the view to the template"})

def date(request):
    return HttpResponse("this page was served at" +str(datetime.now()))

def about(request):
    return HttpResponse("My name is Sumit Kumar Pandey and i learn django in Pluralsight")


# Create your views here.
