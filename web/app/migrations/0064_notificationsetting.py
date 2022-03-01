# Generated by Django 2.2.27 on 2022-03-30 12:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0063_auto_20220318_2317'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('config_json', models.TextField(blank=True, default='')),
                ('enabled', models.BooleanField(default=True)),
                ('notify_on_failure_alert', models.BooleanField(blank=True, default=True)),
                ('notify_on_account_events', models.BooleanField(blank=True, default=False)),
                ('notify_on_print_done', models.BooleanField(blank=True, default=False)),
                ('notify_on_print_cancelled', models.BooleanField(blank=True, default=False)),
                ('notify_on_filament_change', models.BooleanField(blank=True, default=False)),
                ('notify_on_other_events', models.BooleanField(blank=True, default=False)),
                ('notify_on_heater_status', models.BooleanField(blank=True, default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'name')},
            },
        ),
    ]
