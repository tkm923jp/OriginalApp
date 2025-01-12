from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import User,Schedule
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.utils.dateparse import parse_date
from datetime import date
from django.db.models import IntegerField, OuterRef, Subquery, Value
from django.db.models.functions import Coalesce

class ScheduleListView(LoginRequiredMixin, ListView):
    # model = Schedule
    template_name = 'schedules.html'

    # LEFT JOINのようなクエリセットを取得
    def get_queryset(self):
    # リクエストから 'date' パラメータを取得し、日付形式にパース
        selected_date = parse_date(self.request.GET.get('selected_date', str(date.today())))
        if selected_date is None:
            selected_date = date.today()  # パース失敗時は今日の日付を使用

        schedule_key_subquery = Schedule.objects.filter(
            calendar_day=selected_date,
            idnumber=OuterRef('idnumber')
        ).order_by('idnumber').values('id')[:1]
            
    # 最新の更新日付を持つスケジュールデータをサブクエリで取得
        schedule_first_subquery = Schedule.objects.filter(
            calendar_day=selected_date,
            idnumber=OuterRef('idnumber')
        ).order_by('idnumber').values('first_schedule')[:1]

        schedule_second_subquery = Schedule.objects.filter(
            calendar_day=selected_date,
            idnumber=OuterRef('idnumber')
        ).order_by('idnumber').values('second_schedule')[:1]

        schedule_third_subquery = Schedule.objects.filter(
            calendar_day=selected_date,
            idnumber=OuterRef('idnumber')
        ).order_by('idnumber').values('third_schedule')[:1]

        schedule_fourth_subquery = Schedule.objects.filter(
            calendar_day=selected_date,
            idnumber=OuterRef('idnumber')
        ).order_by('idnumber').values('fourth_schedule')[:1]

        contact_subquery = Schedule.objects.filter(
            calendar_day=selected_date,
            idnumber=OuterRef('idnumber')
        ).order_by('idnumber').values('contact')[:1]

        queryset = User.objects.annotate(
            schedule_key=Coalesce(Subquery(schedule_key_subquery, output_field=IntegerField()), Value(0, output_field=IntegerField())),
            schedule_first=Coalesce(Subquery(schedule_first_subquery), Value('')),
            schedule_second=Coalesce(Subquery(schedule_second_subquery), Value('')),
            schedule_third=Coalesce(Subquery(schedule_third_subquery), Value('')),
            schedule_fourth=Coalesce(Subquery(schedule_fourth_subquery), Value('')),
            contact=Coalesce(Subquery(contact_subquery), Value(''))
        ).order_by('group', 'idnumber')

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
    template_name = 'users.html'

class UserCreateView(LoginRequiredMixin,CreateView):
    model = User
    fields = '__all__'

class UserUpdateView(LoginRequiredMixin,UpdateView):
    model = User
    fields = '__all__'
    template_name_suffix = '_update_form'

class UserDeleteView(LoginRequiredMixin,DeleteView):
    model = User
    success_url = reverse_lazy('users')


class ScheduleCreateView(CreateView):
    model = Schedule
    fields = '__all__'

class ScheduleUpdateView(LoginRequiredMixin,UpdateView):
    model = Schedule
    fields = '__all__'
    template_name_suffix = '_update_form'
    
class LoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

class LogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'login.html'