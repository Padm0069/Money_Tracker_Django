# Generated by Django 4.0.3 on 2022-03-30 08:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_bill_group_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='friend1',
        ),
        migrations.RemoveField(
            model_name='friend',
            name='friend2',
        ),
        migrations.AddField(
            model_name='friend',
            name='friend_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='Friend', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='friend',
            name='user_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='Current', to=settings.AUTH_USER_MODEL),
        ),
    ]
