from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from gvozdje.models import Gvozdje, Mreza, User


def home(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def gvozdje(request):
    gvozdje = Gvozdje.objects.all()
    total_gvozdje = gvozdje.count()
    kg = Gvozdje.objects.filter(jedinicaMere='kg').count()
    cena = Gvozdje.objects.filter(cena_DIN=85).count()
    return render(request, 'gvozdje/gvozdje.html', {'gvozdje': gvozdje, 'total_gvozdje':total_gvozdje, 'kg':kg, 'cena':cena})

def mreza(request):
    mreza = Mreza.objects.all()
    total_mreza = mreza.count()
    dime = Mreza.objects.filter(dimenzijeKocke = '15x15cm').count()
    dimenzije=Mreza.objects.filter(dimenzijeKocke= '10x10cm').count()
    return render(request, 'gvozdje/mreza.html', {'mreza': mreza, 'total_mreza':total_mreza, 'dime':dime, 'dimenzije':dimenzije})

def user(request):
    user = User.objects.all()
    total_users = user.count()
    email = User.objects.exclude(email = '@gmail.com').count
    return render(request, 'gvozdje/user.html', {'user': user, 'total_users':total_users, 'email':email})