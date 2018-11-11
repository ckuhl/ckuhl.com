from django.urls import path

from . import views


app_name = 'portfolio'

urlpatterns = [
    path('', views.index, name='index'),

    # individual projects: lowest priority since they're a catchall
    path('<path:project_url>/assets/<str:res_url>', views.project_res),
    path('<path:project_url>/', views.project, name='project'),
]
