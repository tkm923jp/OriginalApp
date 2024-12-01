from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import User,Schedule
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.utils.dateparse import parse_date
from datetime import date

class ScheduleListView(LoginRequiredMixin, ListView):
    model = Schedule
    template_name = 'schedule_list.html'

    # LEFT JOINのようなクエリセットを取得
    def get_queryset(self):
        # GETパラメータから動的に日付を取得
        selected_date_str = self.request.GET.get('selected_date', None)
        
        if selected_date_str:  # 日付が指定されていればパース
            selected_date = parse_date(selected_date_str)
        else:  # 指定されていなければ今日の日付をデフォルトに
            selected_date = date.today()

        queryset = Schedule.objects.filter(calendar_day=selected_date)\
            .select_related('idnumber')\
            .order_by('idnumber__group')  # 班順でソート
        return queryset

    # テンプレートで利用するデータを追加
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # GETパラメータに基づく selected_date をコンテキストに追加
        selected_date_str = self.request.GET.get('selected_date', None)
        if selected_date_str:
            context['selected_date'] = selected_date_str
        else:
            context['selected_date'] = date.today().isoformat()  # デフォルトで今日
        
        return context


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
    success_url = reverse_lazy('user_list')


class ScheduleCreateView(CreateView):
    model = Schedule
    fields = '__all__'

class LoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

class LogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'login.html'