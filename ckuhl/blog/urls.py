from django.urls import path

from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.root, name='index'),
    path('archive/', views.archive, name='archive'),
    path('rss/', views.rss, name='rss'),
    path('tag/<str:tag_name>/', views.tags, name='tags'),

    # redirected URLs
    path('index/', views.old_archive, name='old_archive'),

    # individual posts: lowest priority since they're a catchall
    path('<path:post_url>/', views.post, name='post'),
]
