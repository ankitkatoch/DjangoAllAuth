from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('dashboard/', include('djangoallauthapp.urls')),
    path('chat/', include('chat.urls')),
    path('', TemplateView.as_view(template_name="home.html")),
]
