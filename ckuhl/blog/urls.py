from django.urls import path

from blog import feeds, views

app_name = 'blog'

urlpatterns = [
    path('', views.root, name='index'),
    path('archive/', views.archive, name='archive'),
    path('rss/', feeds.BlogPostRssFeed(), name='rss'),

    # redirected URLs
    path('index/', views.old_archive, name='old_archive'),

    # post resources here since they are a more specific catchall
    path(
        '<path:post_url>/assets/<str:res_url>',
        views.post_res,
        name='post_assets'
    ),
    # individual posts placed last since they are the least specific catchall
    path('<path:post_url>/', views.post, name='post'),
]
