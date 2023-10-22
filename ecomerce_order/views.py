from django.shortcuts import render, redirect
from .forms import UserOrderForm
from .models import Order, OrderDetail
from ecomerce_products.models import Product
from django.contrib.auth.decorators import login_required
# from zeep import Client
from django.http import HttpResponse
# Create your views here.

""" add user order """


@login_required(login_url='/login')
def add_user_order(request):
    form = UserOrderForm(request.POST or None)
    if form.is_valid():
        order = Order.objects.filter(
            owner_id=request.user.id, is_paid=False).first()
        if order is None:
            order = Order.objects.create(
                owner_id=request.user.id, is_paid=False)
        product_id = form.cleaned_data.get('product_id')
        count = form.cleaned_data.get('count')
        if count < 0:
            count = 1
        product = Product.object.get_by_id(productId=product_id)
        order.orderdetail_set.create(
            product_id=product.id, price=product.price, count=count)
        return redirect(f'/products/{product.id}/{product.title.replace(" ", "-")}')
    return redirect('/')


""" open user order """


@login_required(login_url='/login')
def open_user_order(request):
    context = {
        'order': None,
        'details': None,
        'total': 0
    }
    open_order: Order = Order.objects.filter(
        owner_id=request.user.id, is_paid=False).first()
    if open_order is not None:
        context['order'] = open_order
        context['details'] = open_order.orderdetail_set.all()
        context['total'] = open_order.get_total_price()
    return render(request, 'order/open_user_order.html', context)


""" remove order item """


@login_required(login_url='/login')
def remove_order_itme(request, *args, **kwargs):
    detail_id = kwargs.get('detail_id')
    if detail_id is not None:
        order_detail = OrderDetail.objects.get_queryset().get(
            id=detail_id, order__owner_id=request.user.id)
        if order_detail is not None:
            order_detail.delete()
            return redirect('/open_order')


""" zarin pal """
# MERCHANT = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
# amount = 1000  # Toman / Required
# description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
# email = 'email@example.com'  # Optional
# mobile = '09123456789'  # Optional

# client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
# # Important: need to edit for realy server.
# CallbackURL = 'http://localhost:8000/verify/'


# def send_request(request):
#     result = client.service.PaymentRequest(
#         MERCHANT, amount, description, email, mobile, CallbackURL)
#     if result.Status == 100:
#         return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
#     else:
#         return HttpResponse('Error code: ' + str(result.Status))


# def verify(request):
#     if request.GET.get('Status') == 'OK':
#         result = client.service.PaymentVerification(
#             MERCHANT, request.GET['Authority'], amount)
#         if result.Status == 100:
#             return HttpResponse('Transaction success.\nRefID: ' + str(result.RefID))
#         elif result.Status == 101:
#             return HttpResponse('Transaction submitted : ' + str(result.Status))
#         else:
#             return HttpResponse('Transaction failed.\nStatus: ' + str(result.Status))
#     else:
#         return HttpResponse('Transaction failed or canceled by user')
