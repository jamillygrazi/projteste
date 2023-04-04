from django.shortcuts import render
#from django.http import HttpResponse
from forms
from .models import Person

# Create your views here.
def home(request):
    #return HttpResponse("<h1> Olá mundo Ufra!</h1>")
    return render(request, 'base.html')

def principal(request):
    return render(request, 'principal.html')
def login(request):
    return render(request, 'login.html')


def create_doc(request):
    return render(request, 'create_doc.html')

def read_doc(request):
    return render(request, 'read_doc.html')

def pedidos(request):
    return render(request, 'pedidos.html')
def menu(request):
    return render(request, 'menu.html')
def pagamentos(request):
    return render(request, 'pagamentos.html')

def person_creat(request):
    person_form = PersonForm(request.Post or None, request.FILES or None )

 if person_form.is_valid():
     person = person_form.save(commit=False)
     person.save()
     return render(request, 'person_creat.html', {'person_form':person_form})

 def person_read(request):
     persons = Person.objects.all()
     return render(request, 'person_read.html', {'persons':persons})

