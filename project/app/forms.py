from django import forms
from .models import Card, Word


class CardForm(forms.ModelForm):
    ru_word = forms.CharField(label='На русском')
    en_word = forms.CharField(label='На английском')
    pic = forms.ImageField(label='Картинка')

    class Meta:
        model = Card
        fields = ['ru_word', 'en_word', 'pic']


class WordForm(forms.ModelForm):
    ru_word = forms.CharField(label='На русском')
    en_word = forms.CharField(label='На английском')

    class Meta:
        model = Word
        fields = ['ru_word', 'en_word']
