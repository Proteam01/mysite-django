"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import beer_list, delete_beer, home, new_beer, edit_beer, delete_beer, search_beer
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('beer_list',beer_list,name='beer_list'),
    path('new_beer',new_beer,name='new_beer'),
    path('edit_beer/<int:beer_id>',edit_beer,name="edit_beer"),
    path('delete_beer/<int:beer_id>',delete_beer,name='delete_beer'),
    path('search_beer',search_beer,name='delete_beer'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html')),
    path('logout', auth_views.logout_then_login),
]
