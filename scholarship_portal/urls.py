"""scholarship_portal URL Configuration

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
from scholarship.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('admin_login', admin_login, name='admin_login'),
    path('admin_home', admin_home, name='admin_home'),
    path('view_users', view_users, name='view_users'),
    path('delete_user/<int:pid>', delete_user, name='delete_user'),
    path('providers_pending', providers_pending, name='providers_pending'),
    path('providers_accepted', providers_accepted, name='providers_accepted'),
    path('providers_rejected', providers_rejected, name='providers_rejected'),
    path('providers_all', providers_all, name='providers_all'),

    path('change_status/<int:sid>', change_status, name='change_status'),





    path('provider_login', provider_login, name='provider_login'),
    path('provider_signup', provider_signup, name='provider_signup'),
    path('provider_home', provider_home, name='provider_home'),

    path('user_login', user_login, name='user_login'),
    path('user_signup', user_signup, name='user_signup'),
    path('user_home', user_home, name='user_home'),

    path('Logout', Logout, name='Logout')

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
