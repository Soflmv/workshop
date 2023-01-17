from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.views.generic import FormView, ListView
from django.contrib.auth import get_user_model

from .forms import CustomerForm, ManagerForm, MasterForm, WorkerForm
from .mixins import ApplicationMixin, CustomerLoginRequiredMixin
from .models import Application, Parts
from users.models import Role, CustomUser

from django.shortcuts import render
from .forms import EmailForm
from django.core.mail import send_mail
from django.conf import settings


User = get_user_model()


class DetailApplicationView(CustomerLoginRequiredMixin, ApplicationMixin, View):
    """Детальный просмотр заявок"""
    template_name = 'main/detail_users_all.html'

    def get_form(self, application, data=None):
        """Возвращаем форму в соответствии с ролью пользователя"""
        user_form = {
            Role.CUSTOMER: None,
            Role.MANAGER: ManagerForm(data=data, instance=application),
            Role.MASTER: MasterForm(data=data, instance=application),
            Role.WORKER: WorkerForm(data=data, instance=application),
        }

        return user_form.get(self.request.user.role)

    def post(self, request, pk):
        _filter = self._get_repair_filter(self.request.user)
        application = get_object_or_404(Application, pk=pk, **_filter)
        form = self.get_form(application, data=request.POST)
        if form.is_valid():
            users = list(application.users.all())
            form.save()
            application.users.add(request.user, *users)

            return redirect('all_application')
        context = {'application': application,
                   'form': form
                   }

        return render(request, self.template_name, context)

    def get(self, request, pk):
        _filter = self._get_repair_filter(self.request.user)
        application = get_object_or_404(Application, pk=pk, **_filter)
        context = {'application': application,
                   'form': self.get_form(application)}

        return render(request, self.template_name, context)


class ListApplicationView(CustomerLoginRequiredMixin, ApplicationMixin, ListView):
    """Отображение всех заявок"""
    template_name = 'main/all_application.html'
    model = Application
    paginate_by = 23

    def get_queryset(self):
        """Возвращаем заявки согласно статусу пользователя"""
        _filter = self._get_repair_filter(self.request.user)
        return Application.objects.filter(**_filter).order_by('-pk')


class CreateApplicationView(CustomerLoginRequiredMixin, FormView):
    """Создание и проверка правильности заполнения новой заявки аутентифицированным пользователем"""
    template_name = 'main/create_application.html'
    form_class = CustomerForm
    success_url = '/main/all_application/'

    def form_valid(self, form):
        application = form.save()
        application.users.add(self.request.user)
        return super().form_valid(form)


class ClientAllView(CustomerLoginRequiredMixin, ListView):
    """Отображение всех пользователей"""
    model = CustomUser
    template_name = 'main/client_all.html'
    paginate_by = 23

    def get_queryset(self):
        return CustomUser.objects.filter(role='CUSTOMER').order_by('-id')


class EmployeesAllView(CustomerLoginRequiredMixin, ListView):
    """Отображение всех сотрудников"""
    model = CustomUser
    template_name = 'main/employees_all.html'
    paginate_by = 23

    def get_queryset(self):
        return CustomUser.objects.exclude(role='CUSTOMER').order_by('-last_login')


class StockView(CustomerLoginRequiredMixin, ListView):
    """Склад запчастей"""
    model = Parts
    template_name = 'main/stock.html'
    paginate_by = 23

    def get_queryset(self):
        return Parts.objects.all()


class ArchiveView(CustomerLoginRequiredMixin, ListView):
    """Архив выполненных заявок"""
    model = Application
    template_name = 'main/archive.html'
    paginate_by = 23

    def get_queryset(self):
        return Application.objects.filter(status__istartswith='INTO_ARCHIVE')


# Отправка сообщения на почту о завершении работ
def send_email(request):

    messageSent = False

    if request.method == 'POST':

        form = EmailForm(request.POST)

        # проверить, являются ли данные из формы правильными
        if form.is_valid():
            cd = form.cleaned_data
            subject = "Ваша заявка на ремонт автомобиля выполнена!"
            message = cd['message']

            # отправить письмо получателю
            send_mail(subject, message,
                      settings.DEFAULT_FROM_EMAIL, [cd['recipient']])

            messageSent = True

    else:
        form = EmailForm()

    return render(request, 'main/send_email.html', {'form': form, 'messageSent': messageSent})
