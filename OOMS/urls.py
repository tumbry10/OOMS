"""OOMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls.static import static
from OOMS import settings
from dashboard import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),
    path('manage_admin', views.manage_admin, name='manage_admin'),
    path('add_admin', views.add_admin, name='add_admin'),
    path('user_login', views.user_login, name='user_login'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('manage_staff', views.manage_staff, name='manage_staff'),
    path('add_staff', views.add_staff, name='add_staff'),
]+ static(settings.STATIC_URL, document_root= settings.STATICFILES_DIRS) +static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

