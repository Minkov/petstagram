from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_text',)
        widgets = {
            'comment_text': forms.Textarea(
                attrs={
                    'placeholder': 'Add comment...',
                })
        }


class SearchForm(forms.Form):
    search_text = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search by pet name...',
            },
        )
    )