# Generated by Django 4.0.3 on 2022-03-30 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_friend_group_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='group_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.group'),
        ),
    ]
