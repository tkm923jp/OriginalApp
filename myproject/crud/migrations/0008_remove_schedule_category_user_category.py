# Generated by Django 4.2.16 on 2024-10-12 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0007_timehour_timeminutes_schedule_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='category',
        ),
        migrations.AddField(
            model_name='user',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='crud.category'),
            preserve_default=False,
        ),
    ]
