from django.urls import path
from .views import AllFeeds

urlpatterns=[
    path("", AllFeeds.as_view()),
    path("<str:username>", AllFeeds.as_view())
]