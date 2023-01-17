from django import forms
from django.contrib.auth import get_user_model

from .models import Application, CarBrand, PlacesToWork, TypeRepair, Parts, Status
from users.models import Role


User = get_user_model()


class CustomerForm(forms.ModelForm):
    """Модель отображения заявок пользователю"""
    car = forms.ModelChoiceField(
        empty_label='Бренд автомобиля',
        widget=forms.Select(attrs={'class': 'new_application_car'}),
        queryset=CarBrand.objects.all(),
    )
    car_vin = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'new_application_car',
                                      'placeholder': 'VIN-номер, 17 символов'}),
    )
    year = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'new_application_car',
                                      'placeholder': 'Год выпуска'}),
    )
    state_number = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'new_application_car',
                                      'placeholder': 'Рег. номер'}),
    )
    name_client = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'new_application_car',
                                      'placeholder': 'Ваше имя'}),
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'new_application_desc',
                                     'placeholder': 'Описание поломки'}),
    )

    class Meta:
        model = Application
        fields = ['car', 'car_vin', 'year', 'state_number', 'name_client', 'description']


class ManagerForm(forms.ModelForm):
    """Модель отображения заявок менеджеру"""
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'manager_description'}),
        label='',
    )
    time_to_work = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'class': 'manager_time_to_work'}),
        help_text='Время начала ремонта',
        label='',
    )
    completion_time = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={'readonly': 'readonly', 'class': 'manager_completion_time'}),
        help_text='Время завершения ремонта',
        label='',
    )
    status = forms.ChoiceField(
        widget=forms.RadioSelect(attrs={'class': 'manager_application'}),
        label='Статус заявки',
        choices=[
            item for item in Status.choices if item[0] in 'CONFIRMED'
        ]
    )

    class Meta:
        model = Application
        fields = ['description', 'time_to_work', 'completion_time', 'status']


class EmailForm(forms.Form):
    """Отправка Email уведомления на почту клиента"""
    recipient = forms.EmailField(label='Email клиента')
    message = forms.CharField(widget=forms.Textarea, label='Сообщение')


class MasterForm(forms.ModelForm):
    """Модель отображения заявок мастеру"""
    places_to_work = forms.ModelChoiceField(
        widget=forms.Select(attrs={'class': 'master_places_to_work'}),
        queryset=PlacesToWork.objects.all(),
        help_text='Место ремонта',
        label='',
    )
    type_repair = forms.ModelChoiceField(
        widget=forms.Select(attrs={'class': 'master_type_repair'}),
        queryset=TypeRepair.objects.all(),
        help_text='Тип ремонта',
        label='',
    )
    parts = forms.ModelMultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'master_parts'}),
        queryset=Parts.objects.all(),
        help_text='Запчасти',
        label='',
    )
    users = forms.ModelMultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'master_users'}),
        queryset=User.objects.filter(role=Role.WORKER),
        help_text='Выбрать механиков',
        label='',
    )
    completion_time = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'class': 'master_completion_time'}),
        help_text='Время завершения ремонта',
        label='',
    )
    status = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'master_application_status'}),
        help_text='Статус заявки',
        label='',
        choices=[
            item for item in Status.choices if item[0] in ('READY_TO_WORK',
                                                           'RE_REPAIR',
                                                           'VERIFICATION')
        ]

    )

    class Meta:
        model = Application
        fields = ['places_to_work', 'type_repair',  'parts', 'users', 'completion_time', 'status']


class WorkerForm(forms.ModelForm):
    """Модель отображения заявок работнику"""
    status = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'worker_application_status'}),
        label='Статус заявки',
        choices=[
            item for item in Status.choices if item[0] in ('PROGRESS', 'TESTS')
        ]
    )

    class Meta:
        model = Application
        fields = ['status']
