from django.db import models
from common.models import CommonModel

# caption: 게시글 내용
# contentImg: 게시글 이미지
# likesNum: 좋아요 갯수
# reviewsNum: 댓글 갯수

# USER - foreign key
class Feed(CommonModel):
    caption = models.CharField(max_length=1000, default="") # 게시글 내용
    contentImg = models.URLField(blank=True) # 게시글 이미지
    likesNum = models.PositiveIntegerField(default=0) # 좋아요 갯수
    reviewsNum = models.PositiveIntegerField(default=0) # 리뷰 갯수

    # 1:N (User:Feed), N이 ForeignKey를 가진다.
    user = models.ForeignKey(
        "users.User",
        # user가 지워졌을 때
        on_delete=models.CASCADE, # 유저 삭제시 -> 게시글 삭제됨.
        related_name="feeds" # revers accesor에서 불러올 이름 
        # (users.feed_set.all() = users.feeds.all())
    )

    def __str__(self) -> str:
        return self.caption
