from django.urls import path
from .views import (HomePage, RegisterApiView, LoginApiView,
                     UserApiView, RefreshApiView, LogoutApiView)

urlpatterns = [
    path('', HomePage.as_view()),
    path('register', RegisterApiView.as_view()),
    path('login', LoginApiView.as_view()),
    path('user',UserApiView.as_view()),
    path('refresh',RefreshApiView.as_view()),
    path('logout',LogoutApiView.as_view()),
]
