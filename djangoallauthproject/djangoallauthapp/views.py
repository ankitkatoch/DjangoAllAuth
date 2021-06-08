from django.contrib.auth.models import User
from django.shortcuts import render


# Create your views here.
def home(request):
    # params = User.objects.all()
    return render(request, 'home.html')


def user_dashboard(request):
    data = User.objects.all()
    return render(request, 'djangoallauthapp/user_dashboard.html',{'data':data})
