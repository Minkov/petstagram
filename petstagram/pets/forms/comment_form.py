from django import forms

from petstagram.pets.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(
                attrs= {
                    'class': 'form-control rounded-2',
                    'is_required': True,
                },
            ),
        }
