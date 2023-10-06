from django.urls import path
from . import views #lets us reference our views function by importing this module

#URLConf module - need to import this into the main url config for this project
urlpatterns = [
    path('hello/', views.say_hello) #passing a reference to say_hello() function, not calling it + we want to end our routes with a forward slash
]