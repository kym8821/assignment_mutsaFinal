from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
   class Meta:
      model = Article #어떤 모델 쓸거야? : Article
      fields = [ # 사용할 필드들 : Article의 title과 content 사용
         'title', 
         'content', 
         #'author', 글 작성시 다른 사람 도용 가능 --> 빼는 것이 좋다.
      ]