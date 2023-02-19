from django.db import models
from common.models import CommonModel

class Review(CommonModel):
    content = models.URLField(blank=False) # 댓글 내용
    like = models.PositiveIntegerField(default=0) # 댓글 좋아요

    # 하나의 댓글 작성자는 딱 1명만 가능
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE # 유저를 삭제하면 댓글도 지워짐
    )
    
    # 게시글