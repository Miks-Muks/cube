
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

from core import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('shop.urls')),
                  path('__debug__/', include('debug_toolbar.urls')),
                  path('ckeditor/', include('ckeditor_uploader.urls')),
                  path('api-auth/', include('rest_framework.urls')),
                  path('api/v1/', include('api.urls')),
                  path('company/', include('news.urls')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "Куб administration"
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

