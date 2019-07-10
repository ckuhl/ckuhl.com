from django.contrib import admin
from django.urls import include, path

import _commons.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('etc/', include('etc.urls')),
    path('s/', include('shortlink.urls')),

    # This must go last since it will capture any URL including the above
    path('', include('core.urls')),
]

# Default error page override
handler404 = _commons.views.page_not_found
