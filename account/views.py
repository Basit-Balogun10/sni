from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from account.tokens import account_activation_token

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, UpdateView
from django.core.mail import send_mail
from django.conf import settings

from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string

from account.models import Account
from account.forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm
from blog.models import BlogPost


def send_activation_email(request, current_site, user):
    subject = 'Activate Your Synergy Network International Account'
    message = render_to_string('registration/account_activation_email.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
    })
    send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email, ])

    domain = current_site.domain
    encoded_email = urlsafe_base64_encode(force_bytes(user.email))
    messages.success(request, "A verification link has been sent to the email you provided, please use the link sent to confirm your email and complete registration.<br><br>Didn't see the email? <a class=\"font-weight-bold\" href=\"http://" + domain + "/resend_activation_email/" + encoded_email + "\">Resend email activation link</a>", extra_tags='safe')

    return redirect('login')

def registration_view(request):
    user = request.user
    if user.is_authenticated:
        return redirect("sni_app:sni_home")
    context = {}

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.is_active = False
            new_user.save()
            current_site = get_current_site(request)
            return send_activation_email(request, current_site, new_user)
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


class ActivateAccount(View):
    
    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = Account.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, Account.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.profile.email_confirmed = True
            user.firstname = user.firstname.capitalize()
            user.lastname = user.lastname.capitalize()
            user.save()
            # email = user.email
            # raw_password = user.password
            # account = authenticate(email=email, password=raw_password)
            # login(request, account)
            messages.success(request, ('Account Activated Successfully'))
            subject = 'Your Synergy Network International Account Has Been Activated'
            message = render_to_string('registration/appreciation_email.html', {'user': user,})
            send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email, ])
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, ('The confirmation link was invalid, possibly because it has already been used or your account has already been confirmed.'))
            return redirect('home')

class ResendActivationEmail(View):
    
    def get(self, request, target):
        user_email = force_text(urlsafe_base64_decode(target))
        user = Account.objects.get(email=user_email)
        current_site = get_current_site(request)
        return send_activation_email(request, current_site, user)



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
            email = request.POST['email']
            acct = Account.objects.get(email=email)
            if acct.profile.email_confirmed == False:
                current_site = get_current_site(request)
                domain = current_site.domain
                encoded_email = urlsafe_base64_encode(force_bytes(email))
                messages.error(request, "Sorry, you cannot sign in with these details as the email is yet to be confirmed.<br><br>Didn't see the email? <a class=\"font-weight-bold\" href=\"http://" + domain + "/resend_activation_email/" + encoded_email + "\">Resend email activation link</a>", extra_tags='safe')

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
