from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

import core.urls
import user.urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/", include(user.urls, namespace="user")),
    path("", include(core.urls, namespace="core")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
