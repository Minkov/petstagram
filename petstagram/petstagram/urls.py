from django.contrib import admin
from django.core.mail import send_mail
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

'''
HOST network
    127.0.0.1 (host)
    docker container (web)
        127.0.0.1 (web)
        links:
        - postgres
    docker contaienr (db)
        127.0.0.1

127.0.0.1 (host) != 127.0.0.1 (web) != 127.0.0.1 (db)
postgres (web) == 127.0.0.1 (db)
        
'''