from django.db import models
from datetime import *
from django.contrib.auth.models import User
from django.db.models import Sum

# Create your models here.
class Author(models.Model): # наследуемся от класса Model
    authorUser = models.OneToOneField(User, on_delete =models.CASCADE)
    ratingAuthor = models.IntegerField(default = 0)

    def update_rating(self):
        postRat = self.post_set.all().aggregate(postRating=Sum('ratingPost'))
        print('postRat', postRat)
        pRat = 0
        pRat += postRat.get('postRating')

        commentRat =self.authorUser.comment_set.all().aggregate(commentRating=Sum('ratingComment'))
        comRat = 0
        comRat += commentRat.get('commentRating')

        print(pRat,' + ',comRat)
        self.ratingAuthor = pRat * 3 + comRat
        self.save()
    
    def __str__(self):
        return self.authorUser.username

    

class Category(models.Model):
    nameCategory = models.CharField(max_length= 64, unique=True )

    def __str__(self): 
        return self.nameCategory

class Post(models.Model):
    authorPost = models.ForeignKey(Author, on_delete =models.CASCADE)
    NEWS = 'NW' 
    ARTICLE = 'AR'
    POST_CHOISE = (
       (NEWS, 'Новость'),
       (ARTICLE, 'Статья')
    )
    typePost = models.CharField(max_length=2, choices=POST_CHOISE, default=NEWS)
    datetimePost = models.DateTimeField(auto_now_add=True)
    categoryPost =models.ManyToManyField(Category, through='PostCategory')
    titlePost = models.CharField(max_length= 128)
    textPost = models.TextField()
    ratingPost = models.IntegerField(default = 0)

    def __str__(self):
        return self.titlePost+' '+self.textPost[0:50]+' '+str(self.datetimePost.strftime("%Y-%m-%d"))

    def like(self):
        self.ratingPost += 1
        self.save()

    def dislike(self):
        self.ratingPost -= 1
        self.save()

    def preview(self):
        return self.textPost[0:50]+'...'


class PostCategory(models.Model):
    PostPC = models.ForeignKey(Post, on_delete =models.CASCADE)
    CategoryPC = models.ForeignKey(Category, on_delete =models.CASCADE)

class Comment(models.Model):
    postComment = models.ForeignKey(Post, on_delete =models.CASCADE)
    userComment = models.ForeignKey(User, on_delete =models.CASCADE)
    textComment = models.TextField()
    datetimeComment = models.DateTimeField(auto_now_add=True)
    ratingComment = models.IntegerField(default = 0)

    def like(self):
        self.ratingComment += 1
        self.save()

    def dislike(self):
        self.ratingComment -= 1
        self.save()