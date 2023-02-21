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