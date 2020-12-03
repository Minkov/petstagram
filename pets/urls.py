from django.urls import path

from pets.views import list_pets, details_or_comment_pet, like_pet, edit_pet, delete_pet, create_pet

urlpatterns = [
    path('', list_pets, name='list pets'),
    path('detail/<int:pk>/', details_or_comment_pet, name='pet details or comment'),
    path('like/<int:pk>/', like_pet, name='like pet'),
    path('edit/<int:pk>/', edit_pet, name='edit pet'),
    path('delete/<int:pk>/', delete_pet, name='delete pet'),
    path('create/', create_pet, name='create pet'),
]
