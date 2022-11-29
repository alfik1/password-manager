"""password_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from api.views import PasswordView,ApiOverview,add_password,view_passwords,update_pasword

router=DefaultRouter()
router.register("passwords",PasswordView,basename="passwords"),


urlpatterns = [
    path("admin/", admin.site.urls),
    path('token/',views.obtain_auth_token),
    path ("",ApiOverview,name="home"),
    path('create/',add_password, name='add-password'),
    path('all/', view_passwords, name='view_password'),
    path('update/<int:pk>/',update_pasword, name='update-password'),

]+router.urls
