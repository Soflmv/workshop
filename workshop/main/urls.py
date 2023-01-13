from django.urls import path

from .views import CreateApplicationView, ListApplicationView, DetailApplicationView, ClientAllView, EmployeesAllView, \
    SendEmailView, Stock

urlpatterns = [
    path('all_application/', ListApplicationView.as_view(), name='all_application'),
    path('create_application/', CreateApplicationView.as_view(), name='create_application'),
    path('detail_application/<int:pk>/', DetailApplicationView.as_view(), name='detail_application'),
    path('client_all/', ClientAllView.as_view(), name='client_all'),
    path('employees_all/', EmployeesAllView.as_view(), name='employees_all'),
    path('send_email/', SendEmailView.as_view(), name='send_email'),
    path('stock/', Stock.as_view(), name='stock')
]
