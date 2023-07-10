from django.urls import path
from .views import index, like_functionality, share_functionality, comment_functionality

urlpatterns = [
    path('', index, name="index"),
    path('like/<int:photo_id>', like_functionality, name="like"),
    path('share/<int:photo_id>', share_functionality, name="share"),
    path('comment/<int:photo_id>', comment_functionality, name="comment"),
]
