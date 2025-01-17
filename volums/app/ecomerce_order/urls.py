from django.urls import path
from .views import add_user_order, open_user_order, remove_order_itme
urlpatterns = [
    path('add-user-order', add_user_order),
    path('open_order', open_user_order),
    path('remove_order_item/<detail_id>', remove_order_itme)
    # path('request', send_request, name='request'),
    # path('verify', verify, name='verify')
]
