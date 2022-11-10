from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from first import views
from django.views.static import serve

urlpatterns = (
    [
        path('', include("first.urls")),
        path('admin/', admin.site.urls),
        path('api-auth/', include('rest_framework.urls')),
        path('download/', views.home),
        re_path(r'^download/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)