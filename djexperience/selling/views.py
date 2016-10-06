from django.shortcuts import render


def selling_form(request):
    return render(request, 'selling/selling_form.html')
