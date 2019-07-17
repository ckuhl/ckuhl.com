from django.urls import path

from . import views

app_name = 'core'
urlpatterns = [
    # Redirects
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),

    # Live pages
    path('robots.txt', views.robots_txt, name='robots_txt'),
    path('', views.root, name='home'),
]
