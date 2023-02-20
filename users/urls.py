from django.urls import path
from .views import Users, PublucUser, Login, JWTLogin, MyInfo

urlpatterns=[
    path("", Users.as_view()), # 회원가입
    path("login", Login.as_view()), # 로그인
    path("jwt", JWTLogin.as_view()), # JWT 로그인
    path("myinfo", MyInfo.as_view()), # JWT 로그인
    path("<str:username>", PublucUser.as_view()), # 회원조회
]