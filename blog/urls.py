from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.ArticleList.as_view(), name='articles'),
    url(r'^category/$', views.CategoryList.as_view(), name='categories'),
    url(r'^category/(?P<slug>[\w-]+)/$', views.ArticleCategoryListView.as_view(), name='category_detail'),
    url(r'^post/(?P<slug>[\w-]+)/$', views.ArticleView.as_view(), name='article_detail'),

]
