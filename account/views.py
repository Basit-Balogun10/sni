from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from account.forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm
from blog.models import BlogPost


def registration_view(request):
    user = request.user
    if user.is_authenticated:
        return redirect("sni_app:sni_home")
    context = {}

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('blog:index')
        else:
            form.initial = {
                "email": request.POST.get('email'),
                "username": request.POST.get('username'),
                "password1": request.POST.get('password1'),
                "password2": request.POST.get('password2'),
                "firstname": request.POST.get('firstname'),
                "lastname": request.POST.get('lastname'),
            }
            context['registration_form'] = form
            
    else:
        form = RegistrationForm()
        context['registration_form'] = form

    return render(request, 'account/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')


def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("sni_app:sni_home")

    if request.method == "POST":
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect("/")
        else:
            form.initial = {
                "email": request.POST.get('email'),
                "password": request.POST.get('password')
            }

    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form

    return render(request, "account/login.html", context)


def account_view(request):
    if not request.user.is_authenticated:
        return redirect("login")

    context = {}
    if request.method == "POST":
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.initial = {
                "email": request.POST.get('email'),
                "username": request.POST.get('username'),
                "firstname": request.POST.get('firstname'),
                "lastname": request.POST.get('lastname'),
            }
            form.save()
            context['success_message'] = "Updated"
        else:
            pass
            
    else:
        form = AccountUpdateForm(

            initial={
                "email": request.user.email,
                "username": request.user.username,
                "firstname": request.user.firstname,
                "lastname": request.user.lastname,
            }
        )

    context['account_form'] = form

    blog_posts = BlogPost.objects.filter(author=request.user)
    context['blog_posts'] = blog_posts

    return render(request, "account/account.html", context)


def must_authenticate_view(request):
    user = request.user
    if user.is_authenticated:
        return redirect("sni_app:sni_home")
    return render(request, 'account/must_authenticate.html', {})
