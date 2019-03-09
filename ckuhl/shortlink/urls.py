from django.urls import path

from . import views

app_name = 'shortlink'
urlpatterns = [
    path('', views.root, name='root'),
    path('out/<path:outbound_link>/', views.outbound, name='outbound_link'),
    path('ImageBlockX/', views.image_block_x, name='image-block-x'),
    path('MIPS-VM/', views.mips_vm, name='mips-vm'),
]
