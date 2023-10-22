import itertools
from django.shortcuts import render

from ecomerce_slider.models import Slider
from ecomerce_setting.models import SiteSetting
from ecomerce_products.models import Product


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


""" home page """


def home_page(request):
    sliders = Slider.objects.all()
    most_visit_product = Product.object.order_by(
        '-visit_count').all()[:8]
    latest_products = Product.object.order_by('-id').all()[:8]
    context = {
        'title': 'home page',
        'sliders': sliders,
        'most_visit': my_grouper(4, most_visit_product),
        'latest_products': my_grouper(4, latest_products)
    }
    return render(request, 'home-page.html', context)


""" header """


def header(request):
    context = {
        'title': 'this is my title'
    }
    return render(request, 'shared/Header.html', context)


""" footer """


def footer(request):
    site_setting = SiteSetting.objects.first()
    context = {
        'about_us': 'thsi is my first django project',
        'setting': site_setting
    }
    return render(request, 'shared/Footer.html', context)


""" about page """


def about_page(request):
    site_stting = SiteSetting.objects.first()
    context = {
        'setting': site_stting
    }
    return render(request, 'about_page.html', context)