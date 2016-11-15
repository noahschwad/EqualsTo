"""equalsto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from .views import HomePageView, LoginView, LogOutView, SignUpView

urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
    # homepage
    url('^$', HomePageView.as_view(), name='home'),
    #sign up
    url(r'^accounts/register/$', SignUpView.as_view(), name='signup'),
    #setup login view
    url(r'^accounts/login/$', LoginView.as_view(), name='login'),
    #logout
    url(r'^accounts/logout/$', LogOutView.as_view(), name='logout'),   
]
