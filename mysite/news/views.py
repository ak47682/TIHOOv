from django.shortcuts import render

from .models import Article

def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    #相当于完成一次select，同时将结果存在a_list当中
    
    context = {'year': year, 'article_list': a_list}
    return render(request, 'news/year_archive.html', context)