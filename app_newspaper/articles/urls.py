from django.urls import path
from .views import (
    ArticleDeleteView,
    ArticleListView,
    ArticleDetailView,
    ArticleUpdateView,
    ArticleCreateView,
)

urlpatterns = [
    path('', ArticleListView.as_view(), name='articles_site'),
    path("<int:pk>/edit/", ArticleUpdateView.as_view(), name='article_edit'),
    path("<int:pk>/delete/", ArticleDeleteView.as_view(), name='article_delete'),
    path("<int:pk>/", ArticleDetailView.as_view(), name='article_details'),
    path('new/', ArticleCreateView.as_view(), name='article_new'),

]
