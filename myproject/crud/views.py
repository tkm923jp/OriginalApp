from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import User,Schedule
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm

class TopView(TemplateView):
    template_name = "top.html"

class UserListView(LoginRequiredMixin,ListView):
    model = User

class UserCreateView(LoginRequiredMixin,CreateView):
    model = User
    fields = '__all__'

class UserUpdateView(LoginRequiredMixin,UpdateView):
    model = User
    fields = '__all__'
    template_name_suffix = '_update_form'

class UserDeleteView(LoginRequiredMixin,DeleteView):
    model = User
    success_url = reverse_lazy('list')

class ScheduleListView(ListView):
    model = Schedule

class ScheduleCreateView(CreateView):
    model = Schedule
    fields = '__all__'

class LoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

class LogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'login.html'