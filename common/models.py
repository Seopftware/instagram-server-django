from django.db import models

class CommonModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True) 

    class Meta:
        abstract = True # DB에 테이블을 추가하는 것을 원하지 않는다.