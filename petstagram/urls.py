from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('accounts/', include('accounts.urls')),
                  path('admin/', admin.site.urls),
                  path('', include('common.urls')),
                  path('pets/', include('pets.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
