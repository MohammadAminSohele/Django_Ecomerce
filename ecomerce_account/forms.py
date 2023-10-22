from django import forms
from django.contrib.auth.models import User
from django.core import validators

""" edit user form """


class editUserForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'لطفا نام خود را وارد نمایید', 'class': 'form-control'}),
        label='نام'
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
                               'placeholder': 'لطفا نام خانوادگی خود را وارد نمایید', 'class': 'form-control'}),
        label='نام خانوادگی'
    )


""" login form """


class login_form(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'enter your username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'enter your password'})
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        is_exists_user = User.objects.filter(username=username).exists()
        if not is_exists_user:
            raise forms.ValidationError('کاربری با این مشخصات وجود ندارد')
        return username


""" register form """


class register_form(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'نام کاربری خود را وارد کنید'}),
        validators=[
            validators.MaxLengthValidator(
                limit_value=20, message='تعداد کاراکترهای وارد شده نمیتواند بیشتر از 20 باشد'),
            validators.MinLengthValidator(
                limit_value=8, message='تعداد کاراکترهای وارد شده نمیتواند کمتر از 8 باشد')
        ]
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'ایمیل خود را وارد کنید'}),
        validators=[
            validators.EmailValidator('ایمیل وارد شده نامعتبر است')
        ]
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'پسورد خود را وارد کنید'})
    )
    re_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'پسورد خود را دوباره وارد کنید'})
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        is_exist_user_byUsername = User.objects.filter(username=username)
        if is_exist_user_byUsername:
            raise forms.ValidationError(
                'کاربری با این مشخصات قبلا ثبت نام کرده است')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('ایمیل وارد شده تکراری میباشد')
        return email

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        if password != re_password:
            raise forms.ValidationError('پسورد وارد شده مغایرت دراد')
        return password
