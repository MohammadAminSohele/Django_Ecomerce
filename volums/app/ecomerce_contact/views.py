from django.shortcuts import render
from .forms import ContactForm
from .models import ProductContact
from ecomerce_setting.models import SiteSetting

# Create your views here.

""" contact page """
def ContactUs(request):
    form=ContactForm(request.POST or None)
    if form.is_valid():
        full_name=form.cleaned_data.get('full_name')
        email=form.cleaned_data.get('email')
        subject=form.cleaned_data.get('subject')
        text=form.cleaned_data.get('text')
        ProductContact.objects.create(full_name=full_name,email=email,subject=subject,text=text)
        form=ContactForm()
    site_setting=SiteSetting.objects.first()
    context={
        'title':'ارتباط با ما',
        'form':form,
        'setting':site_setting
    }
    return render(request,'contact_us/contact_page.html',context)