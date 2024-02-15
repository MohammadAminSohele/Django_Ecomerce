from django.urls import path

from .views import product_list, product_detail, search_product_list, product_list_ByCatagories, product_catagories_render_partial

urlpatterns = [
    path('', product_list.as_view()),
    path('search', search_product_list.as_view()),
    path('catagory/<catagory_name>', product_list_ByCatagories.as_view()),
    path('<productId>/<name>', product_detail),
    path('product_catagories_partial', product_catagories_render_partial,
         name='product_catagories_partial')
]
""" 


searcg
<catagory_name>
products/<productId>/<name>

"""
