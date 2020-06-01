from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='app-name'),
    path('home', views.home, name='app-home'),
    path('createaccount', views.createaccount, name='app-createaccount'),
]
