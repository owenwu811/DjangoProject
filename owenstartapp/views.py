from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#this is a request handler without a template or html
# a view function takes a request and returns a response, so you can call it a request handler
#a template is something the user sees in django

def say_hello(request):
    #pull data from db, transform data, or send email in real world example use cases
    #instance of httpresponse class
    return HttpResponse('Hello World') #we need to map this view to a url

#left off at 32:00