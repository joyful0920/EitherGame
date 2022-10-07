from dataclasses import field
from django import forms
from django import forms
from .models import Game, Comment


class GameForm(forms.ModelForm):

    class Meta:
        model = Game
        fields = '__all__'


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ('article',)