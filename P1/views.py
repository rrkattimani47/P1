from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("hello world")#HttpResponse(HTML tag as an argument)

def home(request):
    return HttpResponse("<h1>Welcome to homepage<h1>")

def html_demo1(request):
        return render(request,"first.html")

def html_demo2(request):
        return render(request,"directory/second.html")

def html_third(request):
    return render(request,"directory/third.html",context={'data':"Rashmi",'name':'Ritu'})

def html_fourth(request):
    fruits=['apple','strawberry','banana','mango','watermelon','orange','kiwi']
    return render(request,"directory/fourth.html",{'fruits':fruits})

def html_fifth(request):
    return render(request,"directory/fifth.html",{'a':10,'b':99})

def urls_data(request,name):
    return HttpResponse("<h1>{}</h1>".format(name))

def xy(request,xy):
    z=xy.split(" ")
    sum=int(z[0])+ int(z[1])
    return HttpResponse(str(sum))

def ab(request,a,b):
    sum=int(a)+int(b)
    return HttpResponse(str(sum))