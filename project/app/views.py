from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Card, Word
from .forms import CardForm, WordForm


def home(request):
    return render(request, "index.html")


class CardListView(ListView):
    model = Card
    template_name = 'cards.html'


class WordListView(ListView):
    model = Word
    template_name = 'words.html'


def cards_upload_form(request):
    if request.method == 'POST':
        form = CardForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            form.save()
            return redirect('app:cards')
    else:
        form = CardForm()
    return render(request, 'cards-upload.html', {'form': form})


def words_upload_form(request):
    if request.method == 'POST':
        form = WordForm(data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('app:words')
    else:
        form = WordForm()
    return render(request, 'words-upload.html', {'form': form})
