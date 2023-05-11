from django.shortcuts import render
from article.models import Article

def index(request):
  articles = Article.objects.all() # 워낙은 모든 댓글을 갖고오는 것은 안됨... 서버 터짐
  # --> 하려면 몇 개씩 가져와서 뿌려주는 방식으로 ㄱㄱ
  return render(request, 'index.html', {'articles': articles})