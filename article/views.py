from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArticleForm
from .models import Article


def new(request):
    form = ArticleForm()

    if request.method == 'POST':
        form = ArticleForm(request.POST)

        if form.is_valid():
            #article에 form.save 할 때 commit을 False로 해서 임시로 저장
            #form.save 와 save의 차이를 알아보자
            article = form.save(
                commit = False
            )

            article.author = request.user
            article.save()
            return redirect('article:detail', id=article.id)
        
    return render(request, 'new.html', {'form': form})


def detail(request, id):
    article = get_object_or_404(Article, pk=id)
    # id를 통해서 Article 모델에서 article 받아옴

    # 'article':article로 detail.html에 보내줌.
    return render(request, 'detail.html', {'article': article})


def edit(request, id):
    article = get_object_or_404(Article, pk=id)

    form = ArticleForm(instance=article)
    #ArticleForm의 instance를 article로 하여 article에 해당하는 form을 가져옴

    if request.method == 'POST':
      form = ArticleForm(request.POST, instance=article)
      #POST 방식으로 article에 해당하는 form 가져옴

      if form.is_valid():#form이 유효한 form이라면
        article = form.save()#db에 저장
        return redirect('article:detail', id=article.id)#detail 페이지로 id를 갖고 ㄱㄱ

    #form : 입력 받아주는 폼 // article : 기사
    return render(request, 'edit.html', {'form': form, 'article': article})


def destroy(request, id):
   article = get_object_or_404(Article, pk=id)

   article.delete()

   return redirect('main:index')