# Create your views here.
from datetime import datetime

from django.http import HttpResponse
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import View
from .forms import LogForm



# def index(request):
#     return HttpResponse("Hello, world. This is the index view of Demoapp.")
def index(request):
    path = request.path
    method = request.method
    content = ''' 
<center><h2>Testing Django Request Response Objects</h2> 
<p>Request path : " {}</p> 
<p>Request Method :{}</p></center> 
'''.format(path, method)
    return HttpResponse(content)

def homepage(request):
    return HttpResponse("Welcome to little lemon")

def menu(request):
    menu_items = {'mains' :[
        {'name':'greek yougart','price' : '12'},
        {'name': 'soft drink', 'price': '10'},
        {'name': 'tomato', 'price': '9'},
        {'name': 'onion', 'price': '5'},
        {'name': 'mater', 'price': '2'},
        {'name': 'garlic', 'price': '1'},
        {'name': 'ginger', 'price': '20'},
     ]}
    return render(request,'menu.html',menu_items)

def display_date(request):
    date_joined = datetime.today().year
    return HttpResponse(date_joined)

def pathview(request, name, id):
    return HttpResponse("Name:{} UserID:{}".format(name, id))


def qryview(request):
    name = request.GET['name']
    id = request.GET['id']
    return HttpResponse("Name:{} UserID:{}".format(name, id))

def myview(request):
    return HttpResponsePermanentRedirect(reverse('demoapp:login'))


def login(request):
    context = {}
    # context["get_url_path"] = reverse("demoapp:login")
    # user_id = request.POST.get('id')
    # name = request.POST.get('name')
    # # save in DB
    # # return success message
    # context = {"user_id": user_id, "name": name}
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            print("hello")
            # process the form data
        else:
            return HttpResponse("Form submitted with invalid data")
    return render(request, "form.html", context=context)


class MyView(View):

    def get(self, request):
        return HttpResponse('result')

    def post(self, request):
        return HttpResponse('result')


def form_view(request):
    form = LogForm()
    if request.method == "POST":
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return  render(request, 'home.html', context)

