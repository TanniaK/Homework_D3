from django_filters import FilterSet, CharFilter , Filter 
from .models import *

# class UserFilter(Filter):
#     def filter(self, qs, value):
#         return qs.authorUser_set.filter(value)


class NewsFilter(FilterSet):
    #user__author = CharFilter(lookup_expr='icontains')
    #category__category = CharFilter(lookup_expr='icontains')  
    #user_name = UserFilter('username') 

    class Meta:
        model = Post
       
        
        fields = {
                 'authorPost__authorUser__username' : ['icontains'],                 
                 'datetimePost' : ['gt'],
        }

