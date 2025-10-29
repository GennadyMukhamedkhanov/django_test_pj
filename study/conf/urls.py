from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from conf import settings
from conf.yasg import urlpatterns as yasg_url

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include("api.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += yasg_url
