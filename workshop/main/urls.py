from django.urls import path
from . import views

from .views import CreateApplicationView, ListApplicationView, DetailApplicationView, ClientAllView, EmployeesAllView, \
    StockView, ArchiveView

urlpatterns = [
    path('all_application/', ListApplicationView.as_view(), name='all_application'),
    path('create_application/', CreateApplicationView.as_view(), name='create_application'),
    path('detail_application/<int:pk>/', DetailApplicationView.as_view(), name='detail_application'),
    path('client_all/', ClientAllView.as_view(), name='client_all'),
    path('employees_all/', EmployeesAllView.as_view(), name='employees_all'),
    path('send_email/', views.send_email, name='send_email'),
    path('stock/', StockView.as_view(), name='stock'),
    path('archive_application/', ArchiveView.as_view(), name='archive_application')
]

