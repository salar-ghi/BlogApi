from django.urls import path
from . import views
from .views import ArticleList , ArticleDetails

urlpatterns = [
    # path('articles/', views.articleList, name='articlelist'),
    # path('articles/<slug:slug>', views.article_details, name='article_details')

    path("articles/",  ArticleList.as_view() , name='articlelist'),
    path("articles/<slug:slug>",  ArticleDetails.as_view() , name='articledetails')
]