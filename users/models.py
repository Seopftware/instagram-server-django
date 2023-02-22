from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    profileImg = models.URLField(blank=True) # 프로필 이미지
    profileIntroduce = models.CharField(max_length=150, default="") # 프로필 소개글
    followerNumber = models.PositiveIntegerField(default=0) # 팔로우 수