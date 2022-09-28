from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('petstagram.common.urls')),
    path('accounts/', include('petstagram.accounts.urls')),
    path('pets/', include('petstagram.pets.urls')),
    path('photos/', include('petstagram.photos.urls')),
]

'''
After `startapp APP_NAME`

1. Create `APP_NAME/urls.py` with empty `urlpatterns`
2. Include `APP_NAME/urls.py` into project's urls.py
3. Add `APP_NAME` to `INSTALLED_APPS` in settings.py
'''
