from django.contrib import admin
from django.urls import path, include
from .views import user_dashboard
app_name = 'djangoallauthapp'

urlpatterns = [
    path('', user_dashboard, name='user_dashboard')

]
