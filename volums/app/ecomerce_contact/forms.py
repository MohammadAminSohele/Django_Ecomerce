from django import forms
from django.core import validators
""" contact form """
class ContactForm(forms.Form):
    full_name=forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'نام و نام خانوادگی خود را وارد کنید','class':'form-control'}),
        label='نام و نام خانوادگی',
        validators=[
            validators.MaxLengthValidator(150,'نام و نام خانوادگی نمی تواند بیش از 150 کاراکتر باشد')
        ]
    )

    email=forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder':'ایمیل خود را وارد کنید','class':'form-control'}),
        label='ایمیل',
        validators=[
            validators.MaxLengthValidator(100,'ایمیل خود نمی تواند بیش از 100 کاراکتر باشد')
        ]
    )


    subject=forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'عنوان خود را وارد کنید','class':'form-control'}),
        label='عنوان',
        validators=[
            validators.MaxLengthValidator(200,'عنوان خود نمی تواند بیش از 200 کاراکتر باشد')
        ]
    )


    text=forms.CharField(
        widget=forms.Textarea(attrs={'placeholder':'متن پیام خود را وارد کنید','class':'form-control','row':8}),
        label='متن پیام',
    )

