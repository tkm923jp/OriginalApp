# Generated by Django 4.2.16 on 2024-10-12 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0012_remove_schedule_name_alter_schedule_calendar_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='fast_schedule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crud.schedulename', verbose_name='AM①'),
        ),
    ]
