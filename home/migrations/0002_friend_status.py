# Generated by Django 4.0.3 on 2022-03-22 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='status',
            field=models.CharField(default='PENDING', max_length=20),
        ),
    ]
