from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from Education import views




urlpatterns = [
    path('', views.Educationhome, name='Educationhome'),
    path('<str:slug>', views.Educationpost, name="Educationpost"),

]
