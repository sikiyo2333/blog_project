from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from  blog.models import *
# Create your views here.


def index(request):
    article_list = Article.objects.order_by('-datetime')
    paginator = Paginator(article_list,5)
    page = int(request.GET.get('page',1))
    article_list = paginator.page(page)
    return render(request, 'index.html', locals())

def article(request):
       id = request.GET.get('id',None)
       print id
       article = Article.objects.get(pk = id)
       return render(request,'article.html',{'article':article})

def news(request):
	return render(request,'news.html')
