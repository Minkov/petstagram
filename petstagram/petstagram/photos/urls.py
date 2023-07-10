from django.urls import path, include
from .views import photo_details, photo_edit, photo_delete, \
        PhotoAddView

urlpatterns = [
    # photos/
    path('add/', PhotoAddView.as_view(), name='photo add'),
    path('<int:pk>/', include([
        path('', photo_details, name='photo details'),
        path('edit/', photo_edit, name='photo edit'),
        path('delete/', photo_delete, name='photo delete'),
    ]))
]
