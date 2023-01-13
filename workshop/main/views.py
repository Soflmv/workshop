from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import FormView, ListView
from django.contrib.auth import get_user_model

from .forms import CustomerForm, ManagerForm, MasterForm, WorkerForm
from .mixins import ApplicationMixin
from .models import Application, Parts
from users.models import Role, CustomUser

User = get_user_model()


class DetailApplicationView(ApplicationMixin, View):
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


class ListApplicationView(ApplicationMixin, ListView):
    """Отображение всех заявок"""
    template_name = 'main/all_application.html'
    model = Application
    paginate_by = 23

    def get_queryset(self):
        """Возвращаем заявки согласно статусу пользователя"""
        _filter = self._get_repair_filter(self.request.user)
        return Application.objects.filter(**_filter).order_by('-pk')


class CreateApplicationView(FormView):
    """Создание и проверка правильности заполнения новой заявки пользователем"""
    template_name = 'main/create_application.html'
    form_class = CustomerForm
    success_url = '/main/all_application/'

    def form_valid(self, form):
        application = form.save()
        application.users.add(self.request.user)
        return super().form_valid(form)


class ClientAllView(ListView):
    """Отображение всех пользователей"""
    model = CustomUser
    template_name = 'main/client_all.html'

    def get_queryset(self):
        return CustomUser.objects.filter(role='CUSTOMER').order_by('-id')


class EmployeesAllView(ListView):
    """Отображение всех сотрудников"""
    model = CustomUser
    template_name = 'main/employees_all.html'

    def get_queryset(self):
        return CustomUser.objects.exclude(role='CUSTOMER').order_by('-last_login')


class Stock(ListView):
    """Склад запчастей"""
    model = Parts
    template_name = 'main/stock.html'

    def all_price(self, request):

        return render(request, self.template_name)


class SendEmailView(ListView):
    """Отправка сообщения на почту о завершении работ"""
    pass




