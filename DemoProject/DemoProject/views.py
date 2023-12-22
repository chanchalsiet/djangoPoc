from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def handler404(request, exception):
    return HttpResponse("404 : Page not found!<br><br> <button onclick="" href :'';""> go to HomePage</button>")

# def about(request):
#     return render(request,'about.html')