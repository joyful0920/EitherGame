from django.db import models


class Game(models.Model):
    title = models.TextField()
    issue_a = models.TextField()
    issue_b = models.TextField()
    img_url = models.TextField()


class Comment(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    content = models.TextField()
    voted = models.CharField(max_length=30)