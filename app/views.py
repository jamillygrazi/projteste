from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import PersonForm, docForm
from .models import Person, Doc

# Create your views here.
def home(request):
    #return HttpResponse("<h1> Olá mundo Ufra!</h1>")
    return render(request, 'base.html')

def principal(request):
    return render(request, 'principal.html')
def login(request):
    return render(request, 'login.html')

def create_doc(request):
    docs = Doc.objects.all()
    return render(request, 'create_doc.html',
                  {'docs': docs})


def read_doc(request):
    doc_form = docForm(request.POST or
                             None,
                             request.FILES or
                             None)
    if doc_form.is_valid():
        person = doc_form.save(commit=False)
        person.save()
    return render(request, 'read_doc.html',
                  {'doc_form':doc_form})


def pedidos(request):
    return render(request, 'pedidos.html')
def menu(request):
    return render(request, 'menu.html')
def pagamentos(request):
    return render(request, 'pagamentos.html')
def person_create(request):
    person_form = PersonForm(request.POST or
                             None,
                             request.FILES or
                             None)
    if person_form.is_valid():
        person = person_form.save(commit=False)
        person.save()
    return render(request, 'person_create.html',
                  {'person_form':person_form})

def person_read(request):
    persons = Person.objects.all()
    return render(request, 'person_read.html',
                  {'persons':persons})

def person_update(request, id):
    person = get_object_or_404(Person, pk=id)
    person_form = PersonForm(request.POST or
                             None,
                             request.FILES or
                             None,
                             instance=person)
    if person_form.is_valid():
        person = person_form.save(commit=False)
        person.save()

    return render(request,
                  'person_create.html',
                  {"person_form":person_form})

def person_delete(request, id):
    person = get_object_or_404(Person, pk=id)
    person.delete()
    return redirect("read_person")

def doc_delete(request, id):
    doc = get_object_or_404(Doc, pk=id)
    doc.delete()
    return redirect("create_doc")

def doc_update(request, id):
    doc = get_object_or_404(Doc, pk=id)
    doc_form = docForm(request.POST or
                             None,
                             request.FILES or
                             None,
                             instance=doc)
    if doc_form.is_valid():
        doc = doc_form.save(commit=False)
        doc.save()

    return render(request,
                  'read_doc.html',
                  {"doc_form":doc_form})
