from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('s/', include('shortlink.urls')),

    # This must go last since it will capture any URL including the above
    path('', include('core.urls')),
]
