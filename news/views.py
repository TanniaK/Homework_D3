
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.views.generic.base import View # импортируем класс, который говорит нам о том, что в этом представлении мы будем выводить список объектов из БД# импортируем класс получения деталей объекта
from .models import *
from datetime import datetime
from django.core.paginator import Paginator # импортируем класс, позволяющий удобно осуществлять постраничный вывод
from .filters import NewsFilter
from .forms import NewsForm


# Create your views here.
class NewsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = Post.objects.filter(typePost='NW').order_by('-id')
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET,
                                       queryset=self.get_queryset()) 
        return context


class NewsDetail(DetailView):
    model = Post 
    template_name = 'news_id.html' 
    context_object_name = 'news_id' 


class NewsSearch(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'news'
    queryset = Post.objects.filter(typePost='NW').order_by('-id')
    paginate_by = 6

    def get_filter(self):
        return NewsFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *args, **kwargs):
        return {
               **super().get_context_data(*args, **kwargs),
               "filter":self.get_filter(),
        }

class NewsCreateView(CreateView):
    template_name = 'news_create.html'
    form_class = NewsForm
    success_url = '/news/'

class NewsUpdateView(UpdateView):
    template_name = 'news_create.html'
    form_class = NewsForm
    success_url = '/news/'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

class NewsDeleteView(DeleteView):
    template_name = 'news_delete.html'
    queryset =  Post.objects.filter(typePost='NW')
    context_object_name = 'news_id' 
    success_url = '/news/'

    


