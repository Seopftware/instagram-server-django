from django.urls import path
from . import views

urlpatterns = [
    path("", views.Feeds.as_view()),
    path("<str:username>", views.UserFeeds.as_view()), # 회원조회
]