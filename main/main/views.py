from django.shortcuts import render


def welcome_page(request):
    return render(request, 'main/welcome_page.html')
