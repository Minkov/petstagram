from django import forms

from petstagram.pets.models import Pet


class PetForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Pet
        fields = '__all__'
        widgets = {
            'image_url': forms.TextInput(
                attrs={
                    'id': 'img_input',
                }
            )
        }
