from django.shortcuts import render
from .models import General_Chairman, Co_Chair, Secretery_General, Financial_Secretery, Women_Chair, Youth_Chair
# Create your views here.
def chairman(request):
    data = General_Chairman.objects.all().order_by('-votes')

    context = {

        'data': data,
    
        
    }
    
    return render(request, 'members/results.html', context)


def secretery(request):
    data = Secretery_General.objects.all().order_by('-votes')

    context = {

        'data': data,
        
    }
    
    return render(request, 'members/secretery.html', context)


def financial(request):
    data = Financial_Secretery.objects.all().order_by('-votes')

    context = {

        'data': data
        
    }
    
    return render(request, 'members/financial.html', context)


def women(request):
    data = Women_Chair.objects.all().order_by('-votes')

    context = {

        'data': data
        
    }
    
    return render(request, 'members/women.html', context)


def youth(request):
    data = Youth_Chair.objects.all().order_by('-votes')

    context = {

        'data': data
        
    }
    
    return render(request, 'members/youth.html', context)