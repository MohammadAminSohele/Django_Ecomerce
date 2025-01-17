from django.urls import path
from .views import ContactUs

urlpatterns = [
    path('contact_us',ContactUs)
]