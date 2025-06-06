"""
URL configuration for ecomerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from ecomerce import settings
from django.conf.urls.static import static

from .settings import STATIC_ROOT, STATIC_URL, MEDIA_ROOT, MEDIA_URL
from .views import home_page, header, footer, about_page

urlpatterns = [
    path('', home_page),
    path('', include('ecomerce_account.urls')),
    path('products/', include('ecomerce_products.urls')),
    path('', include('ecomerce_contact.urls')),
    path('', include('ecomerce_order.urls')),
    path('about', about_page),
    path('header', header, name='header'),
    path('footer', footer, name='footer'),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=MEDIA_ROOT)
