from django.db import models
from common.models import CommonModel

class Feed(CommonModel):
    img = models.URLField(blank=False) # 게시글 이미지
    content = models.CharField(max_length=150) # 게시글 내용
    like = models.PositiveIntegerField(default=0) # 좋아요

    # 유저
    # 게시글의 소유자는 딱 1명만 가능
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE # 유저를 삭제하면 게시글도 지워짐
    )

def __str__(self) -> str:
    return self.content