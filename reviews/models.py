from django.db import models
from common.models import CommonModel

# caption: 댓글 내용

# USER
# FEED
class Review(CommonModel):
    caption = models.CharField(max_length=150)