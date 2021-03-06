"""P1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from P1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('home',views.home,name='home'),
    path('html_demo1',views.html_demo1,name='html_demo1'),
    path('html_demo2',views.html_demo2,name='html_demo2'),
    path('html_third',views.html_third,name='html_third'),
    path('html_fourth',views.html_fourth,name='html_fourth'),
    path('html_fifth',views.html_fifth,name='html_fifth'),
    path("urls_data/<name>",views.urls_data,name="urls_data"),
    path("xy/<xy>",views.xy,name="xy"),
    path("ab/<a>/<b>",views.ab,name="ab"),
    path('greater/<c>/<d>/<e>',views.greater,name="greater"),
 
    
]
