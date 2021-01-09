from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import RegisterForm, LoginForm


def HomeView(request):
    return render(request, 'home.html')

#
# class Userlogin(View):
#     def __init__(self, **kwargs):
#         super().__init__(kwargs)

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated ',
                                        'successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html' , {'form': form})



class RegisterView(TemplateView):
    template_name = "registration/register.html"

    def dispatch(self, request, *args, **kwargs):
        form = RegisterForm()
        if request.method == 'POST':
            form = RegisterForm(request,'POST')
            if form.is_valid():
                self.create_new_user(form)
                messages.success(request, u'Вы успешно зарегистрировались!')
                return redirect('registration/register.html')

        context = {
            'form': form
        }
        return render(request, self.template_name, context)


    def create_new_user(self, form):
        email = None
        if 'email' in form.cleaned_data:
            email = form.cleaned_data['email']
        User.objects.create_user(form.cleaned_data['username'], email, form.cleaned_data['password'],
                                first_name=form.cleaned_data['first_name'],
                                last_name=form.cleaned_data['last_name'])



class LogoutView(View):
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return redirect('/')



class ProfileView(TemplateView):
    template_name = "registration/profile.html"

