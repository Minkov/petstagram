from django.contrib import admin
from .models import Photo

# Register your models here.


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_of_publication', 'tagged_pets_str',)

    @staticmethod
    def tagged_pets_str(obj):
        return ", ".join([pet.name for pet in obj.tagged_pets.all()])