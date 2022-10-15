from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Produto

def error404(request, exception): #aparecerá apenas com DEBUG = False (produção)
    return render(request, '404.html')

def error500(request): #aparecerá apenas com DEBUG = False (produção)
    return render(request, '500.html')

def produto(request, pk):
    #produto = Produto.objects.get(id = pk)
    produto = get_object_or_404(Produto,id = pk)
    contexto = {
        'prod': produto,
        'curso': 'Programação Web com Python e Django Framework: Essencial',
        'autor' : 'Geek University',
        'plataforma' : 'Udemy',
        }
    print(produto)
    return render(request, 'produto.html',contexto)


def index(request):
    produtos = Produto.objects.all()
    contexto = {
        'produtos' : produtos,
        'curso': 'Programação Web com Python e Django Framework: Essencial',
        'autor' : 'Geek University',
        'plataforma' : 'Udemy',
        }
    return render(request, 'index.html', contexto)


def contato(request):
    #print(request.user.email)

    if str(request.user) == 'AnonymousUser':
        logado = 'não está logado'
    else:
        logado = 'está logado'
    contexto = {
        'curso' : 'Programação web com Python Django',
        'logado' : logado,
        'user' : request.user,
    }
    return render(request, 'contato.html', contexto)




#from django.http import HttpResponse
#def index(request):
#return HttpResponse("Hello, world. You're at the polls index.")
