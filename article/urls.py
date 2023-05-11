from django.urls import path
from .views import new, detail, edit, destroy

app_name = 'article'

urlpatterns = [
  path("new", new, name='new'),#C
  path("<int:id>", detail, name='detail'),#R
  path("edit/<int:id>", edit, name='edit'),#U
  path("destroy/<int:id>", destroy, name='destroy'),#D
]
