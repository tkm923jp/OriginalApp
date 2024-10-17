from django.db import models
from django.urls import reverse

class Timehour(models.Model):
    time_hour = models.CharField(max_length=200,verbose_name='時')

    def __str__(self):
        return self.time_hour
    
class Timeminutes(models.Model):
    time_minutes = models.CharField(max_length=200,verbose_name='分')

    def __str__(self):
        return self.time_minutes

class Schedulename(models.Model):
    schedule_name = models.CharField(max_length=200,verbose_name='予定区分')

    def __str__(self):
        return self.schedule_name

class Category(models.Model):
    name = models.CharField(max_length=200,verbose_name='権限')

    def __str__(self):
        return self.name

class Schedule(models.Model):
    idnumber = models.CharField(max_length=200,verbose_name='社員番号')
    calendar_day = models.DateField(null=True,blank=True,verbose_name='日付')
    fast_schedule = models.ForeignKey(Schedulename, on_delete=models.CASCADE,null=True,blank=True,verbose_name='AM1')
    second_schedule = models.CharField(max_length=200,null=True,blank=True,verbose_name='AM2')
    third_schedule = models.CharField(max_length=200,null=True,blank=True,verbose_name='PM1')
    fourth_schedule = models.CharField(max_length=200,null=True,blank=True,verbose_name='PM2')
    contact = models.CharField(max_length=200,null=True,blank=True,verbose_name='連絡事項')
    def __str__(self):
        return self.idnumber
    
    def get_absolute_url(self):
        return reverse('schedule_list')
    


class User(models.Model):
    idnumber = models.CharField(max_length=200,verbose_name='社員番号')
    name = models.CharField(max_length=200,verbose_name='氏名')
    phonenumber = models.CharField(max_length=200,null=True,blank=True,verbose_name='電話番号')
    email = models.EmailField(max_length=200,null=True,blank=True,verbose_name='メールアドレス')
    group = models.CharField(max_length=200,null=True,blank=True,verbose_name='班')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name='権限')
    def __str__(self):
        return self.name
    
# 新規作成・編集完了時のリダイレクト先
    def get_absolute_url(self):
        return reverse('list')
