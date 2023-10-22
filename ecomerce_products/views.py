import itertools
from django.shortcuts import render
from django.views.generic import ListView
from django.http import Http404

from .models import Product, ProductGallary
from ecomerce_catagory.models import ProductCatagory
from ecomerce_order.forms import UserOrderForm

""" my_grouper """


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))

# detail view


""" product detail """


def product_detail(request, *args, **kwargs):
    selected_productId = kwargs['productId']
    new_order_form = UserOrderForm(request.POST or None, initial={
                                   'product_id': selected_productId})
    product: Product = Product.object.get_by_id(selected_productId)
    if product is None or not product.activate:
        raise Http404('محصول مورد نظر یافت نشد')

    product.visit_count += 1
    product.save()

    galeries = ProductGallary.objects.filter(product_id=selected_productId)
    grouped_galeries = list(my_grouper(3, galeries))

    related_products = Product.object.get_queryset().filter(
        catagories__product=product).distinct()

    grouped_gallery = list(my_grouper(3, related_products))

    context = {
        'title': 'صفحه محصول',
        'product': product,
        'galeries': grouped_galeries,
        'relatedProduct': grouped_gallery,
        'new_order_form': new_order_form
    }

    print(product.tag_set.all())

    return render(request, 'products/product-detail.html', context)

# list view


""" product list """


class product_list(ListView):
    template_name = 'products/product-list.html'
    paginate_by = 4

    def get_queryset(self):
        return Product.object.get_activate_product()


""" search product list """


class search_product_list(ListView):
    template_name = 'products/search-product-list.html'
    paginate_by = 4

    def get_queryset(self):
        request = self.request
        print(request.GET)
        query = request.GET.get('q')
        if query is not None:
            return Product.object.search(query)

        return Product.object.get_activate_product()


""" product list by catagories """


class product_list_ByCatagories(ListView):
    template_name = 'products/product-list.html'
    paginate_by = 4

    def get_queryset(self):
        # print(self.kwargs)
        catagory_name = self.kwargs['catagory_name']
        catagory = ProductCatagory.objects.filter(
            name__iexact=catagory_name).first()
        if catagory is None:
            raise Http404('صفحه مورد نظر یافت نشد')
        return Product.object.get_by_catagory(catagory_name)

# render partial


""" product catagories render partial """


def product_catagories_render_partial(request):
    catagories = ProductCatagory.objects.all()
    context = {
        'catagories': catagories
    }
    return render(request, 'products/product-catagories-render-partial.html', context)
