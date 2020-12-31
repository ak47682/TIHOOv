from django.urls import path

from . import views

urlpatterns = [
    path('hw/create/', views.HomeworkCreate.as_view()),
    path('', views.HomeworkCreate.as_view()),

#urlpatterns = [
    #path('articles/<int:year>/', views.year_archive),
    #path('articles/<int:year>/<int:month>/', views.month_archive),
    #path('articles/<int:year>/<int:month>/<int:pk>/', views.article_detail),
]
#此处会出现报错，原因是因为我们并没有写相应的功能，所以我们要继续添加功能