from django.urls import path

from . import views

app_name = 'etc'

urlpatterns = [
    # Root page
    path('', views.root_page, name='root'),

    # Singleton pages
    path('about/', views.about_page, name='about_singleton'),
    path('contact/', views.contact_page, name='contact_singleton'),
    path('words/', views.words_page, name='words_singleton'),
]
