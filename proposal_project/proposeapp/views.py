from django.shortcuts import render


def love(request):
    return render(request, 'love.html')


def mylove(request):
    return render(request,'accepted.html')
