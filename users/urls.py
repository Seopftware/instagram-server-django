from django.urls import path
from .views import MyInfo, Login, Logout, JWTLogin

urlpatterns=[
    path("myinfo", MyInfo.as_view()),
    path("login", Login.as_view()),
    path("logout", Logout.as_view()),
    path("jwtlogin", JWTLogin.as_view()),
]