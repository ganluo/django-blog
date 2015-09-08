from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Article

def index(request):
    latest_article_list =  Article.objects.order_by('-pub_date')[:3]
    context = {'latest_article_list': latest_article_list}
    return render(request, 'article/index.html', context)

def detail(request, year, month, day, title):
    post = get_object_or_404(Article, title=title)
    return render(request, 'article/detail.html', {'post': post})

def archive(request):
    article_list =  Article.objects.order_by('-pub_date')
    paginator = Paginator(article_list, 5)
    page = request.GET.get('page')

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.paginator(paginator.num_pages)

    context = {'article_list': articles}
    return render(request, 'article/blog.html', context)

def year_archive(request):
    pass

def month_archive(request):
    pass

def day_archive(request):
    pass

def about(request):
    return render(request, 'article/about.html')

def category(request, name):
    article_list = get_list_or_404(Article, category__iexact = name)
    return render(request, 'article/category.html', {'article_list': article_list})


def search(request):
    keyword =  request.GET.get('keyword', '')
    if not keyword.strip() == '':
        query = Q(title__icontains=keyword) | Q(content__icontains=keyword)
        article_list = Article.objects.filter(query)
        return render(request, 'article/search.html', {'article_list': article_list, 'error': 0 == len(article_list)})

    return redirect('/')

