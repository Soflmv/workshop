from django.contrib.auth import get_user_model

from main.models import Status
from users.models import Role

User = get_user_model()


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
