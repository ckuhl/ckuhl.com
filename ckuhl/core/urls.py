from django.urls import path

from . import views

app_name = 'core'
urlpatterns = [
    # Redirects
    path('contact/', views.contact),
    path('about/', views.about),

    # Live pages
    path('robots.txt', views.robots_txt),
    path('', views.root, name='home'),
]
