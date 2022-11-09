from django import forms
from django.core.exceptions import ValidationError

from petstagram.common.models import PhotoLike, PhotoComment
from petstagram.core.form_mixins import DisabledFormMixin
from petstagram.photos.models import Photo


class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ('publication_date', 'user')


class PhotoCreateForm(PhotoBaseForm):
    pass


class PhotoEditForm(PhotoBaseForm):
    class Meta:
        model = Photo
        exclude = ('publication_date', 'photo')


class PhotoDeleteForm(DisabledFormMixin, PhotoBaseForm):
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        if commit:
            self.instance.tagged_pets.clear()  # many-to-many

            Photo.objects.all() \
                .first().tagged_pets.clear()
            PhotoLike.objects.filter(photo_id=self.instance.id) \
                .delete()  # one-to-many
            PhotoComment.objects.filter(photo_id=self.instance.id) \
                .delete()  # one-to-many
            self.instance.delete()

        return self.instance
