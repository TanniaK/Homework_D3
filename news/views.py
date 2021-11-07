from django.views.generic import ListView, DetailView # импортируем класс, который говорит нам о том, что в этом представлении мы будем выводить список объектов из БД# импортируем класс получения деталей объекта
from .models import *
from datetime import datetime

# Create your views here.
class NewsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = Post.objects.filter(typePost='NW').order_by('-id')
    #queryset = Post.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow() 
        return context

class NewsDetail(DetailView):
    model = Post 
    template_name = 'news_id.html' 
    context_object_name = 'news_id' 


