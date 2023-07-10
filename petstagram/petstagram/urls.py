from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include("petstagram.common.urls")),
    path('accounts/', include("petstagram.accounts.urls")),
    path('pets/', include("petstagram.pets.urls")),
    path('photos/', include("petstagram.photos.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
