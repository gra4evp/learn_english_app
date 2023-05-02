from django.db import models


class Card(models.Model):
    ru_word = models.CharField(max_length=30)
    en_word = models.CharField(max_length=30)
    pic = models.ImageField(upload_to='images/')


class Word(models.Model):
    ru_word = models.CharField(max_length=30)
    en_word = models.CharField(max_length=30)
