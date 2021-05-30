from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from blogs.models import Post
from home import views


urlpatterns = [
    path("", views.index, name='home'),
    path('contact', views.contact, name="contact"),
    path('search', views.search, name="search"),
    path('signup', views.handleSignUp, name="handleSignUp"),
    path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
    path('appointment', views.Appointmentadd, name="Appointmentadd"),
    path("Terms_conditions", views.Terms_conditions, name='Terms_conditions'),
    path("Education", views.Education, name='Education'),
    path("Pricing", views.Pricing, name='Pricing'),
    
    ]