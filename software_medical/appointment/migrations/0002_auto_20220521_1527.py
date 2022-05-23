# Generated by Django 3.2.12 on 2022-05-21 13:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appoinment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appoinment',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
