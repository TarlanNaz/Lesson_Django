from django.http import HttpResponse
from django.shortcuts import render


articles = [
   {
       'id': 1,
       'title': 'First news',
       'text': 'This is the worst first article'
   },
   {
       'id': 2,
       'title': 'Second news',
       'text': 'This is the amazing second article'
   }]

# Create your views here.
def index(request):
    return render(request,'news_blog/news_list.html', {'articles': articles})

def get_article(request, article_id,):
    article=None
    for i in articles:
        if i['id'] == article_id:
            article = i
            break

    return render(request, 'news_blog/news_article.html', {'article': article})

def me(request):
    return render(request,'news_blog/about.html',)

#def get_




