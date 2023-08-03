from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

#Модель поста
class Post(models.Model):

    title = models.CharField(max_length=250, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_posts')
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogapp:post_selected', args=[self.pk])

