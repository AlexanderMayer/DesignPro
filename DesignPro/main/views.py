from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.views.generic import CreateView
from .forms import RegisterUserForm
from django.views.generic import TemplateView
from .models import AdvUser
from django.urls import reverse_lazy


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


class BBLoginView(LoginView):
    template_name = 'main/login.html'


@login_required
def profile(request):
    return render(request, 'main/profile.html')


class BBLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'main/logout.html'


class RegisterUserView(CreateView):
    model = AdvUser
    template_name = 'main/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('main:register_done')


class RegisterDoneView(TemplateView):
   template_name = 'main/register_done.html'