from django import forms
from .models import Photo
from .validators import text_underscore_validator

labels = {
    'pet_image': 'Photo file',
    'description': 'Description',
    'location': 'Location',
    'tagged_pets': 'Tag Pets'
}


class PhotoAddForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['pet_image', 'description', 'location', 'tagged_pets']
        labels = labels

class PhotoEditForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['description', 'location', 'tagged_pets']
        exclude = ['pet_image']
        labels = labels


class ExampleForm(forms.Form):
    description = forms.CharField(
        validators=[text_underscore_validator]
    )

# 1. full_clean
# 2. clean fields
# 3. field -> clean
# 4. run validators
# 5. validator(value)
