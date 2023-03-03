from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def home(request):
    #return HttpResponse("<h1> Olá mundo Ufra!</h1>")
    return render(request, 'base.html')


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
