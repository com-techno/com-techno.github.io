from django.shortcuts import render

def main(request):
    return render(request, 'main/main.html')

def about(request):
    return render(request, 'main/abotus.html')

def rules(request):
    return render(request, 'main/rules.html')