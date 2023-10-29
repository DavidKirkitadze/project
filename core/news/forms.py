from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'Name of article'
            }),
            "anons": TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'Anons'
            }),
            "date": DateTimeInput(attrs={
                'class': 'from-control',
                'placeholder': 'Date of bublicate'
            }),
            "full_text": Textarea(attrs={
                'class': 'from-control',
                'placeholder': 'Text article'
            })
        }