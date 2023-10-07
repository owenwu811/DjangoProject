from django.shortcuts import render
from django.http import HttpResponse

def calculate():
    x = 5
    y = 10
    return x

# Create your views here.
#this is a request handler without a template or html
# a view function takes a request and returns a response, so you can call it a request handler
#a template is something the user sees in django

def say_hello(request):
    #x = calculate()
    #pull data from db, transform data, or send email in real world example use cases
    #instance of httpresponse class
    #return HttpResponse('Hello World') #we need to map this view to a url
    return render(request, 'hello.html', {'name': 'Owen'})

#templates in django are used to return html content to the client
#we will use the render function to return html to the client