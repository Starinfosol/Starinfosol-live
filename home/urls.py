from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from blogs.models import Post
from home import views


urlpatterns = [
    path("", views.index, name='home'),
    path('contact', views.contact, name="contact"),
    path("blogs", views.blogs, name='blogs'),
    # path("posts", views.posts, name='posts'),
    path('updates', views.updates, name="updates"),
    path('health', views.health, name='health'),
    path("blog-single", views.blog_single, name='blog-single'),
    path('search', views.search, name="search"),
    path("blog-education", views.blog_education, name='blog-education'),
    path('signup', views.handleSignUp, name="handleSignUp"),
    path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
    path('appointment', views.Appointmentadd, name="Appointmentadd"),
    path("Terms_conditions", views.Terms_conditions, name='Terms_conditions'),
    
    ]