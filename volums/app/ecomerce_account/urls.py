from django.urls import path

from .views import login_page, register_page, log_out, user_account_main_page, edit_user_profile

urlpatterns = [
    path('login', login_page),
    path('register', register_page),
    path('log-out', log_out),
    path('user', user_account_main_page),
    path('user/edit', edit_user_profile),
]
