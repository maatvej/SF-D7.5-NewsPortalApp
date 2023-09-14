from django.urls import path
from .views import (PostsList, PostDetail, PostSearch, NewsCreate, ArticleCreate, PostUpdate, PostDelete,
                    CategoryListView, subscribe)

urlpatterns = [
    path('', PostsList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('search', PostSearch.as_view(), name='post_search'),
    path('postnews', NewsCreate.as_view(), name='news_create'),
    path('postarticle', ArticleCreate.as_view(), name='article_create'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/subscribe', subscribe , name='subscribe'),
]
