from django import forms
from .models import Pet
# from petstagram.pets.models import Pet

# FORM - use when getting data not related to model (not creating model instance)
# MODEL FORM - use when getting data related to model (creating model instance)





class BaseForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'date_of_birth', 'personal_pet_photo']
        #fields = '__all__'  # or [field1, ...]

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Pet name',
                }
            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'placeholder': 'mm/dd/yyyy',
                    'type': 'date'
                }
            ),
            'personal_pet_photo': forms.URLInput(
                attrs={
                    'placeholder': 'Link to image',
                }
            )
        }
        labels = {
            'name': 'Pet name',
            'date_of_birth': 'Date of birth',
            'personal_pet_photo': 'Link to image',
        }


class PetAddForm(BaseForm):
    pass


class PetEditForm(BaseForm):
    pass


class PetDeleteForm(BaseForm):
    hidden_field = forms.CharField(
        widget=forms.HiddenInput(
            attrs={
                'disabled': 'disabled',
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance