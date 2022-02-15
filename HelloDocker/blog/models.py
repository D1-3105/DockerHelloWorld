from django.db import models
from django.contrib.auth import get_user_model


class Blog(models.Model):
    author=models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING)
    title=models.CharField(max_length=255)
    txt=models.TextField()
    date=models.DateTimeField(auto_now=True)
    class Meta:
        unique_together=['author','title','txt']