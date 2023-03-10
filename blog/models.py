from django.db import models
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=110)
    subtitle = models.CharField(max_length=200)
    text = models.TextField(max_length=800)

    def __str__(self):
        return f'{self.title} -+ {self.subtitle}'
    
    def get_absolute_url(self):
        return reverse('blog:article-detail', kwargs={'pk': self.id})