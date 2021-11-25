from django.urls import path
from .views import NewsList, NewsDetail, NewsSearch, NewsCreateView # импортируем наше представление
from .views import NewsDeleteView, NewsUpdateView 
 
urlpatterns = [
   
    path('', NewsList.as_view()), 
    path('<int:pk>', NewsDetail.as_view()),
    path('search/', NewsSearch.as_view()),
    path('add/', NewsCreateView.as_view(), name='news_create'),
    path('<int:pk>/edit/', NewsUpdateView.as_view(), name='news_update'),
    path('<int:pk>/delete/', NewsDeleteView.as_view(), name='news_delete'),

]  