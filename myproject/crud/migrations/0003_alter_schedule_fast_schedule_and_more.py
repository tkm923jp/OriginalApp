# Generated by Django 4.2.16 on 2024-10-10 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_schedule_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='fast_schedule',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='fourth_schedule',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='second_schedule',
            field=models.EmailField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='third_schedule',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
