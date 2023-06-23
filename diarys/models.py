from django.db import models


# Create your models here.
class Page(models.Model):
    # 제목, 내용, 감정 상태, 감정 점수, 작성일
    title = models.CharField(max_length=100)
    content = models.TextField()
    feeling = models.CharField(max_length=50)
    score = models.IntegerField()
    dt_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
