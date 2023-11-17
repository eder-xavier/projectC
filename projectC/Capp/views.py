
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from .models import WithVariation, OutVariation

dados_with_variation = WithVariation.objects.all()
dados_out_variation = OutVariation.objects.all()
dados = list(dados_with_variation) + list(dados_out_variation)

def home(request):
    if 'kic' in request.GET:
        id_pesquisa = request.GET['kic']
        try:
            id_pesquisa = int(id_pesquisa)
            with_variation = WithVariation.objects.filter(kic=id_pesquisa).first()
            out_variation = OutVariation.objects.filter(kic=id_pesquisa).first()

            if with_variation or out_variation:
                return redirect('Capp:pagina_objetos', kic=id_pesquisa)
            else:
                return render(request, 'catalog/notf.html')
        except ValueError:
            return render(request, 'catalog/notf.html')
    else:
        itens_por_pagina = 12
        dados_with_variation = WithVariation.objects.all()
        dados_out_variation = OutVariation.objects.all()
        dados = list(dados_with_variation) + list(dados_out_variation)
        paginator_with = Paginator(dados_with_variation, itens_por_pagina)
        paginator_out = Paginator(dados_out_variation, itens_por_pagina)

        page_number = request.GET.get('page', 1)
        page_number = int(page_number)

        try:
            dados_paginados_with_variation = paginator_with.page(page_number)
            dados_paginados_out_variation = paginator_out.page(page_number)
        except PageNotAnInteger:
            dados_paginados_with_variation = paginator_with.page(1)
            dados_paginados_out_variation = paginator_out.page(1)
        except EmptyPage:
            dados_paginados_with_variation = paginator_with.page(paginator_with.num_pages)
            dados_paginados_out_variation = paginator_out.page(paginator_out.num_pages)

        context = {
            #'dados': dados_paginados,
            'dados_paginados_with_variation': dados_paginados_with_variation,
            'dados_paginados_out_variation': dados_paginados_out_variation,
            }

        return render(request, 'catalog/home/home.html', context)

def pagina_objetos(request, kic):
    lista_de_dados1 = WithVariation.objects.filter(kic=kic)
    lista_de_dados2 = OutVariation.objects.filter(kic=kic)

    total_objetos = len(lista_de_dados1) + len(lista_de_dados2)
    itens_por_pagina = 12
    total_paginas = (total_objetos + itens_por_pagina - 1) // itens_por_pagina

    page_number = request.GET.get('page', 1)
    page_number = int(page_number)

    if page_number < 1:
        page_number = 1
    elif page_number > total_paginas:
        page_number = total_paginas

    indice_inicial = (page_number - 1) * itens_por_pagina
    indice_final = min(indice_inicial + itens_por_pagina, total_objetos)

    lista_pagina_with = lista_de_dados1[indice_inicial:indice_final]
    lista_pagina_out = lista_de_dados2[indice_inicial:indice_final]

    template_name = f'catalog/mid/kic{kic}/page{kic}.html'
    context = {
        'lista_pagina_with': lista_pagina_with,
        'lista_pagina_out': lista_pagina_out,
        'total_paginas': total_paginas,
        'page_number': page_number,
    }
    return render(request, template_name, context)

def pagina_continuacao(request, kic):
    lista_de_dados = WithVariation.objects.filter(kic=kic)

    total_objetos = len(lista_de_dados)
    itens_por_pagina = 12
    total_paginas = (total_objetos + itens_por_pagina - 1) // itens_por_pagina

    page_number = request.GET.get('page', 1)
    page_number = int(page_number)

    if page_number < 1:
        page_number = 1
    elif page_number > total_paginas:
        page_number = total_paginas

    indice_inicial = (page_number - 1) * itens_por_pagina
    indice_final = min(indice_inicial + itens_por_pagina, total_objetos)

    lista_pagina = lista_de_dados[indice_inicial:indice_final]

    template_name = 'catalog/home/home2.html'
    context = {
        'lista_pagina': lista_pagina,
        'total_paginas': total_paginas,
        'page_number': page_number,
    }
    return render(request, template_name, context)
    

