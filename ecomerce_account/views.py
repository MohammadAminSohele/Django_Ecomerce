from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import login_form, register_form, editUserForm

# Create your views here.

""" login page """


def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    form = login_form(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            form.add_error('username', 'this user is not found')
    context = {
        'title': 'login page',
        'form': form
    }
    return render(request, 'account/login-page.html', context)


""" register """


def register_page(request):
    form = register_form(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        User.objects.create_user(
            username=username, email=email, password=password)
        return redirect('/login')

    context = {
        'title': 'register page',
        'form': form
    }
    return render(request, 'account/register-page.html', context)


""" log out """


def log_out(request):
    logout(request)
    return redirect('/login')


""" user account main page """


@login_required(redirect_field_name='/login')
def user_account_main_page(request):
    return render(request, 'account/user_account_main.html', {})


""" edit user page """


@login_required(redirect_field_name='/login')
def edit_user_profile(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    if user is None:
        raise Http404('کاربر مورد نظر یافت نشد')

    edit_user_form = editUserForm(request.POST or None,
                                  initial={'first_name': user.first_name, 'last_name': user.last_name})

    if edit_user_form.is_valid():
        first_name = edit_user_form.cleaned_data.get('first_name')
        last_name = edit_user_form.cleaned_data.get('last_name')

        user.first_name = first_name
        user.last_name = last_name
        user.save()

    context = {'edit_form': edit_user_form}

    return render(request, 'account/edit_user_profile.html', context)


""" user side bar render partial view """


def user_sidebar(request):
    return render(request, 'account/user_sidebar.html', {})
