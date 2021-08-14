from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from core.models import *
from .decorators import *
from store.models import *
from .forms import *


# Create your views here.


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'core/index.html'
    login_url = 'core:user-login'
    redirect_field_name = 'core:user-login'

    def get_context_data(self, **kwargs):
        items = Item.objects.filter(user=self.request.user).order_by('date')
        context = {'items': items}
        return context

    def post(self, request):
        date = request.POST['date']
        items = Item.objects.filter(date=date, user=request.user)
        return render(request, self.template_name, {'items': items})


class UserRegistrationView(CreateView):
    form_class = UserRegistrationForm
    initial = {'key': 'value'}
    template_name = 'core/user_register.html'
    @method_decorator(unauthenticated_user)
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            messages.success(request, 'Account was created for ' + email)
            return redirect('core:user-login')
        return render(request, self.template_name, {'form': form})


class LoginView(TemplateView):
    form_class = UserLogin
    initial = {'key': 'value'}
    template_name = 'core/login.html'
    @method_decorator(unauthenticated_user)
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('core:home')
        else:
            messages.info(request, 'Username OR Password is Incorrect')
        return render(request, 'core/login.html', {'form': form})


def UserLogout(request):
    logout(request)
    return redirect('core:user-login')

