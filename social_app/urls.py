from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth.views import LogoutView
from . import views
from django.views.generic import TemplateView
urlpatterns = [
 path('', TemplateView.as_view(template_name='social_app/index.html')),
 path('accounts/', include('allauth.urls')),
    url(r'^social_app/login',views.login,name='login'),
path('', TemplateView.as_view(template_name='social_app/login.html')),
path(
    'logout/',
    LogoutView.as_view(template_name='social_app/index.html'),
    name='logout'
    ),
path('manage/', views.manage, name='manage'),
    url(r'^dashboard',views.dashboard,name='dashboard'),
    url(r'^getsdata',views.getsdata,name='getsdata'),
    url(r'^getinfo',views.getinfo,name='getinfo'),
    url(r'^getcollect',views.getcollect,name='getcollect'),




]