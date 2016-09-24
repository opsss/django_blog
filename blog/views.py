from django.views import generic
from django.shortcuts import get_object_or_404
from .models import Article, Category


class ArticleList(generic.ListView):
    model = Article
    template_name = 'blog/articles.html'


class ArticleView(generic.DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'blog/article.html'


class CategoryList(generic.ListView):
    model = Category
    template_name = 'blog/category.html'


class ArticleCategoryListView(generic.ListView):
    model = Article
    context_object_name = 'articles_category'
    template_name = 'blog/category_view.html'

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Article.objects.filter(category=self.category)






