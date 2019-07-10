from django.urls import path

from . import views

app_name = 'etc'

urlpatterns = [
    path('words/', views.words_page, name='words'),
]
