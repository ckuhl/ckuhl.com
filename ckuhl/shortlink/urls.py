from django.urls import path

from . import views


app_name = 'shortlink'
urlpatterns = [
    path('', views.root, name='root'),
    path('ImageBlockX/', views.image_block_x, name='image-block-x'),
]
