from django.urls import path, re_path


from .views import ThreadView,  InboxView, IndexView

app_name = 'chat'
urlpatterns = [
    path("global/", IndexView.as_view()),
    path("/", InboxView.as_view()),
    re_path(r"^(?P<username>[\w.@+-]+)", ThreadView.as_view()),
    # path('', users_list, name='users_list')
]
