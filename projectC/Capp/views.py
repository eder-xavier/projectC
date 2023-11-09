
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render,HttpResponse,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import DadosGerais
from django.core.paginator import Paginator
from . import models

#################### HOME PAGES


def home0(request):
    return render(request, 'catalog/home/home.html')

def home(request):
    dados = DadosGerais.objects.all()
    if 'kic' in request.GET:
        id_pesquisa = request.GET['kic']
        try:
            id_pesquisa = int(id_pesquisa)
            dado = DadosGerais.objects.get(kic=id_pesquisa)
            return redirect('Capp:pagina_objetos', kic=id_pesquisa)
        except ValueError:
            return render(request, 'catalog/notf.html')
        except DadosGerais.DoesNotExist:
            return render(request, 'catalog/notf.html')
    else:
        itens_por_pagina = 12
        paginator = Paginator(dados, itens_por_pagina)
    
        # Obter o número da página atual
        page_number = request.GET.get('page', 1)
        page_number = int(page_number)
    
        try:
            dados_paginados = paginator.page(page_number)
        except PageNotAnInteger:
            # Se a página não for um número inteiro, exibir a primeira página
            dados_paginados = paginator.page(1)
        except EmptyPage:
        # Se a página estiver fora do intervalo, exibir a última página
            dados_paginados = paginator.page(paginator.num_pages)
    return render(request, 'catalog/home/home.html', {'dados': dados_paginados})

# ...

def pagina_objetos(request, kic):
    # Obtenha todos os objetos relacionados ao 'kic'
    lista_de_dados = DadosGerais.objects.filter(kic=kic)

    # Número total de objetos
    total_objetos = lista_de_dados.count()

    # Número de itens por página
    itens_por_pagina = 12

    # Calcule o número total de páginas necessárias para exibir os objetos em grupos de 12
    total_paginas = (total_objetos + itens_por_pagina - 1) // itens_por_pagina

    # Obtenha o número da página da consulta de parâmetro GET (se não for fornecido, use 1)
    page_number = request.GET.get('page', 1)
    page_number = int(page_number)

    if page_number < 1:
        page_number = 1
    elif page_number > total_paginas:
        page_number = total_paginas

    # Calcule o índice inicial e final dos objetos a serem exibidos nesta página
    indice_inicial = (page_number - 1) * itens_por_pagina
    indice_final = min(indice_inicial + itens_por_pagina, total_objetos)

    # Obtenha a lista de objetos a serem exibidos nesta página
    lista_pagina = lista_de_dados[indice_inicial:indice_final]

    # Obtenha o objeto correspondente ao KIC selecionado
    objeto_kic = get_object_or_404(DadosGerais, kic=kic)

    template_name = f'catalog/mid/kic{kic}/page{kic}.html'
    context = {
        'lista_pagina': lista_pagina,
        'total_paginas': total_paginas,
        'page_number': page_number,
        'objeto_kic': objeto_kic,
    }
    return render(request, template_name, context)

def pagina_continuacao(request, kic):
    # Obtenha todos os objetos relacionados ao 'kic'
    lista_de_dados = DadosGerais.objects.filter(kic=kic)

    # Número total de objetos
    total_objetos = lista_de_dados.count()

    # Número de itens por página
    itens_por_pagina = 12

    # Calcule o número total de páginas necessárias para exibir os objetos em grupos de 12
    total_paginas = (total_objetos + itens_por_pagina - 1) // itens_por_pagina

    # Obtenha o número da página da consulta de parâmetro GET (se não for fornecido, use 1)
    page_number = request.GET.get('page', 1)
    page_number = int(page_number)

    if page_number < 1:
        page_number = 1
    elif page_number > total_paginas:
        page_number = total_paginas

    # Calcule o índice inicial e final dos objetos a serem exibidos nesta página
    indice_inicial = (page_number - 1) * itens_por_pagina
    indice_final = min(indice_inicial + itens_por_pagina, total_objetos)

    # Obtenha a lista de objetos a serem exibidos nesta página
    lista_pagina = lista_de_dados[indice_inicial:indice_final]

    #template_name = f'mid/kic{kic}/continuacao{kic}.html'
    template_name = 'catalog/home/home2.html'

    context = {
        'lista_pagina': lista_pagina,
        'total_paginas': total_paginas,
        'page_number': page_number,
    }
    return render(request, template_name, context) 

    

