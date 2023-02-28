from django.urls import path
from .views import SignUpUsers, PublicUser, Login, JWTLogin, MyInfo, Logout, KakaoLogin

urlpatterns=[
    path("signup", SignUpUsers.as_view()), # 회원가입
    # path("<str:username>", PublicUser.as_view()), # 회원조회
    path("login", Login.as_view()), # 로그인
    path("jwtlogin", JWTLogin.as_view()), # JWT 로그인
    path("myinfo", MyInfo.as_view()), # 내정보 (나만보기)
    path("logout", Logout.as_view()), # 로그아웃
    path("kakao", KakaoLogin.as_view()), # 카카오 로그인
]