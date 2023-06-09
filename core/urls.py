from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

from core.settings import dev


urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('shop.urls')),
                  path('users/', include('users.urls')),
                  path('__debug__/', include('debug_toolbar.urls')),
                  path('ckeditor/', include('ckeditor_uploader.urls')),

                  path('company/', include('news.urls')),
              ] + static(dev.STATIC_URL, document_root=dev.STATIC_ROOT)
admin.site.site_header = "Куб administration"
urlpatterns += static(dev.MEDIA_URL, document_root=dev.MEDIA_ROOT)


