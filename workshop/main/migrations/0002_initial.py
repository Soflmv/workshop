# Generated by Django 4.1.3 on 2023-01-07 07:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Участники заявки'),
        ),
        migrations.AddField(
            model_name='application',
            name='works',
            field=models.ManyToManyField(related_name='work_repairs', to='main.works', verbose_name='Работы'),
        ),
    ]
