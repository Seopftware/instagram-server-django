from django.urls import path
from .views import AllFeeds, UserNameFeeds

urlpatterns=[
    path("", AllFeeds.as_view()),
    path("<str:username>", UserNameFeeds.as_view())
]