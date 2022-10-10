from django.urls import path, include

from petstagram.pets.views import add_pet, details_pet, edit_pet, delete_pet

urlpatterns = (
    path('add/', add_pet, name='add pet'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', details_pet, name='details pet'),
        path('edit/', edit_pet, name='edit pet'),
        path('delete/', delete_pet, name='delete pet'),
    ]))
)

'''
https://softuni.bg/trainings/3858/python-web-basics-september-2022
'''
