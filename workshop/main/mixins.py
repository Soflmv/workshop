from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import AccessMixin

from main.models import Status
from users.models import Role

User = get_user_model()


class CustomerLoginRequiredMixin(AccessMixin):
    """Убеждаемся, что текущий пользователь аутентифицирован и не является анонимным для создания новой заявки"""

    def dispatch(self, request, *args, **kwargs):
        if (
            request.user.is_authenticated and request.user.role == Role.CUSTOMER
        ):
            return super().dispatch(request, *args, **kwargs)
        elif (
            request.user.is_authenticated and request.user.role == Role.MANAGER
        ):
            return super().dispatch(request, *args, **kwargs)
        elif (
            request.user.is_authenticated and request.user.role == Role.MASTER
        ):
            return super().dispatch(request, *args, **kwargs)
        elif (
            request.user.is_authenticated and request.user.role == Role.WORKER
        ):
            return super().dispatch(request, *args, **kwargs)

        return self.handle_no_permission()


class ApplicationMixin:
    """Миксин для фильтрации заявок по роли пользователя"""
    @staticmethod
    def _get_repair_filter(user: User):
        """Фильтр для роли пользователя"""
        application_filter = {
            Role.CUSTOMER: {
                'users': user
            },
            Role.MANAGER: {
                'status__in': [
                    Status.CREATED,
                    Status.VERIFICATION,
                ]
            },
            Role.MASTER: {
                'status__in': [
                    Status.CONFIRMED,
                    Status.PROGRESS,
                    Status.TESTS,
                    Status.READY_TO_WORK,
                ]
            },
            Role.WORKER: {
                'status__in': [
                    Status.PROGRESS,
                    Status.TESTS,
                    Status.READY_TO_WORK,
                ]
            },
        }
        return application_filter.get(user.role)
