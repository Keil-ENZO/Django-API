from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    author = models.CharField(max_length=64)
    date = models.DateTimeField()


class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)