from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from home import views


urlpatterns = [
    path("", views.index, name='index'),
    path("index.html", views.index, name='index'),
    path('contact', views.contact, name="contact"),
    path('search', views.search, name="search"),
    path('signup', views.handleSignUp, name="handleSignUp"),
    path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
    path("Terms_conditions", views.Terms_conditions, name='Terms_conditions'),
    path("Pricing", views.Pricing, name='Pricing'),
    path('Technical', views.Technical, name="Technical"),
    path('Management', views.Management, name="Management"),
    path('Medicine', views.Medicine, name="Medicine"),
    path('physiotherapy', views.physiotherapy, name="physiotherapy"),
    path('pathology', views.pathology, name="pathology"),
    path('Doctors', views.Doctors, name="Doctors"),
    path('careers', views.careers, name="careers"),
    path('career_field', views.careersadd, name="careersadd"),
    # path('popup', views.popup, name="popup"),
    
    ]