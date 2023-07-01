from django.db import models
from .validators import validate_no_hash, validate_no_numbers, validate_score


# Create your models here.
class Page(models.Model):
    # 제목, 내용, 감정 상태, 감정 점수, 작성일
    title = models.CharField(max_length=100, validators=[validate_no_hash])
    content = models.TextField(validators=[validate_no_hash])
    feeling = models.CharField(max_length=50, validators=[validate_no_numbers])
    score = models.IntegerField(validators=[validate_score])
    dt_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
