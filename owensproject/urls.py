"""
URL configuration for owensproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include #we import include function because it says including another URLconf import include function - READ CAREFULLY

#step 2 of Including another URLconf says add a url to urlpatterns, which is what we do below 
#if a request is sent to owenstartapp/hello, django knows to direct all request that start with owenstartapp, it will chop off everything before /hello and pass it to url configuration module in the owenstartapp app
urlpatterns = [
    path('admin/', admin.site.urls),
    path('owenstartapp/', include('owenstartapp.urls'))
]
