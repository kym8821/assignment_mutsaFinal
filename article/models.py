from django.db import models

class Article(models.Model):
  author = models.ForeignKey(
    'user.User',
    on_delete=models.CASCADE,
  )
  #ForeignKey : 1대다 관계
  title = models.TextField()
  content = models.TextField()

  created_at = models.DateTimeField(
    auto_now_add=True,
  )
  
  updated_at = models.DateTimeField(
    auto_now=True,
  )

