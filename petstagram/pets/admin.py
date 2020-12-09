from django.contrib import admin

from petstagram.pets.models import Pet, Like, Comment


class LikeInline(admin.TabularInline):
    model = Like


class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'name', 'age')
    list_filter = ('type', 'age')
    inlines = (
        LikeInline,
    )

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'pet_id')


admin.site.register(Pet, PetAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like)
