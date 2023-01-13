from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='main/home.html'), name='home'),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('main/', include('main.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

