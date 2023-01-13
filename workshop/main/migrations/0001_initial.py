# Generated by Django 4.1.3 on 2023-01-07 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Бренд автомобиля',
                'verbose_name_plural': 'Бренд автомобиля',
            },
        ),
        migrations.CreateModel(
            name='Parts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Тип детали')),
                ('price', models.IntegerField(default='', verbose_name='Цена детали')),
            ],
            options={
                'verbose_name': 'Тип детали',
                'verbose_name_plural': 'Типы деталей',
            },
        ),
        migrations.CreateModel(
            name='PlacesToWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Место ремонта')),
            ],
            options={
                'verbose_name': 'Место ремонта',
                'verbose_name_plural': 'Места ремонта',
            },
        ),
        migrations.CreateModel(
            name='TypeRepair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Тип ремонта')),
                ('hours', models.PositiveSmallIntegerField(verbose_name='Часов для ремонта')),
            ],
            options={
                'verbose_name': 'Тип работы',
                'verbose_name_plural': 'Типы работ',
            },
        ),
        migrations.CreateModel(
            name='Works',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Тип работы')),
            ],
            options={
                'verbose_name': 'Тип работы',
                'verbose_name_plural': 'Типы работ',
            },
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Описание поломки')),
                ('status', models.CharField(choices=[('CREATED', 'Новая заявка'), ('CONFIRMED', 'Подтверждена менеджером'), ('READY_TO_WORK', 'Готова к работе'), ('PROGRESS', 'Выполняется'), ('VERIFICATION', 'Ремонт выполнен'), ('TESTS', 'На проверку'), ('RE_REPAIR', 'На доработку')], default='CREATED', max_length=50, verbose_name='Статус')),
                ('time_to_work', models.DateTimeField(blank=True, null=True, verbose_name='Время принятия в работу')),
                ('completion_time', models.DateTimeField(null=True, verbose_name='Время завершения ремонта')),
                ('car_vin', models.CharField(max_length=17, null=True)),
                ('year', models.CharField(max_length=30, null=True)),
                ('state_number', models.CharField(max_length=15, null=True)),
                ('name_client', models.CharField(max_length=30, null=True)),
                ('car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='car_repairs', to='main.carbrand', verbose_name='Автомобиль')),
                ('parts', models.ManyToManyField(related_name='part_repairs', to='main.parts', verbose_name='Запчасти')),
                ('places_to_work', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='place_to_application', to='main.placestowork', verbose_name='Место ремонта')),
                ('type_repair', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='type_repairs', to='main.typerepair')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
    ]
