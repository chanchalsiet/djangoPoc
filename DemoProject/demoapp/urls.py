from django.urls import path

from . import views

app_name = 'demoapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.form_view),
    path("login/", views.login, name="login"),
    path('homepage/', views.homepage),
    path('menu/', views.menu),
    path('display_date/', views.display_date),
    path('getuser/', views.qryview, name='qryview'),
]
