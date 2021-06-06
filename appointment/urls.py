from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from appointment import views


urlpatterns = [

    path('appointment', views.Appointmentadd, name="Appointmentadd"),
#     path("handlerequest", views.handlerequest, name="HandleRequest"),
#     path("checkout", views.checkout, name="checkout"),

]
