from django.shortcuts import render, redirect


def main_page(request):
    return render(request, 'main/main.html')


def about_us_page(request):
    return render(request, 'main/abotus.html')


def rules_page(request):
    return render(request, 'main/rules.html')