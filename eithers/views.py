from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST, require_safe

from .models import Game, Comment
from .forms import GameForm, CommentForm


@require_safe
def index(request):
    games = Game.objects.all()
    length = Game.objects.count()
    random = Game.objects.order_by('?').first()
    context = {
        'games': games,
        'length': length,
        'random': random,
    }
    return render(request, 'eithers/index.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.save()
            return redirect('eithers:detail', game.pk)
    else:
        form = GameForm()
    context = {
        'form': form,
    }
    return render(request, 'eithers/create.html', context)


@require_safe
def detail(request, pk):
    game = Game.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = game.comment_set.all()

    if len(comments) != 0:
        left = round(len(comments.filter(voted='primary')) /
                     len(comments) * 100, 2)
        right = 100 - left
    else:
        left, right = 50, 50

    context = {
        'game': game,
        'comment_form': comment_form,
        'comments': comments,
        'left': left,
        'right': right,
    }
    return render(request, 'eithers/detail.html', context)


@require_POST
def comments_create(request, pk):
    game = Game.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.game = game
        comment.user = request.user
        comment.save()
    return redirect('eithers:detail', game.pk)
