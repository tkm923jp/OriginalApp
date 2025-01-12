from django.db import models
from django.urls import reverse

SCHEDULE_CHOICES = [
    ('千代田区', '千代田区'),
    ('中央区', '中央区'),
    ('港区', '港区'),
    ('品川区', '品川区'),
    ('大田区', '大田区'),
    ('会議・打合せ', '会議・打合せ'),
    ('研修', '研修'),
    ('出張', '出張'),
    ('在宅', '在宅'),
    ('休暇', '休暇'),
    ('明休', '明休'),
    ('代休', '代休'),
]
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

class User(models.Model):
    idnumber = models.CharField(max_length=200,verbose_name='社員番号',unique=True)
    name = models.CharField(max_length=200,verbose_name='氏名')
    phonenumber = models.CharField(max_length=200,null=True,blank=True,verbose_name='電話番号')
    email = models.EmailField(max_length=200,null=True,blank=True,verbose_name='メールアドレス')
    group = models.CharField(max_length=200,null=True,blank=True,verbose_name='班')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name='権限')
    def __str__(self):
        return self.name
    
# 新規作成・編集完了時のリダイレクト先
    def get_absolute_url(self):
        return reverse('users')


class Schedule(models.Model):
    idnumber = models.ForeignKey(User, to_field='idnumber', on_delete=models.CASCADE)
    calendar_day = models.DateField(null=True,blank=True,verbose_name='日付')
    first_schedule = models.CharField('AM1',max_length=10,null=True,blank=True,choices=SCHEDULE_CHOICES)
    second_schedule = models.CharField('AM2',max_length=10,null=True,blank=True,choices=SCHEDULE_CHOICES)
    third_schedule = models.CharField('PM1',max_length=10,null=True,blank=True,choices=SCHEDULE_CHOICES)
    fourth_schedule = models.CharField('PM2',max_length=10,null=True,blank=True,choices=SCHEDULE_CHOICES)
    contact = models.CharField(max_length=200,null=True,blank=True,verbose_name='連絡事項')
    def __str__(self):
        return self.idnumber
    
    def get_absolute_url(self):
        return reverse('schedules')
    



