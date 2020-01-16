from django.shortcuts import render, redirect


def new(request):
    return render(request, 'games/new-number.html')
