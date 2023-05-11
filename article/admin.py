from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin): #여기서 admin 커스텀 가능!
    pass
