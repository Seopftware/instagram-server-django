from django.db import models
from django.contrib.auth.models import AbstractUser

# username : 유저 이름 => 기존 어드민에 이미 포함되어 있어서 생성하지 않아도됨.
# profileIntroduce : 유저 프로필 소개글
# profileImg : 유저 프로필 이미지
# followerNum: 유저 팔로워 수
class User(AbstractUser):
    profileImg = models.URLField(blank=True) # 이미지 링크를 첨부하기 위함
    profileIntroduce = models.CharField(max_length=150, default="")
    followerNum = models.PositiveIntegerField(default=0)