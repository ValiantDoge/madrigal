"""Aspire URL Configuration

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import environ

env = environ.Env()
environ.Env.read_env()

urlpatterns = [
    path('', include('website_hr.urls'), name='website'),
    path('resumebuilder/', include('resumebuilder.urls')),
    path('blog/', include('blog.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/', include('authapp.urls')),
    path('admin_panel/', include('admin_panel.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
     #Linkedin Social Login
    path('social-auth/', include('social_django.urls', namespace='social')),
    
    path(env('SECRET_ADMIN_URL') + 'admin/', admin.site.urls),
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "website_hr.views.errorpage"
