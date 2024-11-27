# import django_filters
# from django.shortcuts import render
# from .models import Article
# from .filters import ArticleFilter
# from django_filters.views import FilterView

# class ArticleFilter(django_filters.FilterSet):
#     title = django_filters.CharFilter(lookup_expr="icontains", label='Titre')
#     genre = django_filters.CharFilter(lookup_expr="icontains", label='Genre')

#     class Meta:
#         model = Article
#         fields = ['title', 'genre', 'author', 'publisher']

# class ArticleListView(FilterView):
#     model = Article
#     template_name = 'titles/list.html'
#     filterset_class = ArticleFilter