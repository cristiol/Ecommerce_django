from django.shortcuts import render



def payments_success(request):
    return render(request, 'payments_success.html')
