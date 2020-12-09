from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('accounts/', include('petstagram.accounts.urls')),
                  path('admin/', admin.site.urls),
                  path('', include('petstagram.common.urls')),
                  path('pets/', include('petstagram.pets.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
