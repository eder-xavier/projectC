from django.shortcuts import render
from django.http import JsonResponse
import lightkurve as lk
import base64
import matplotlib.pyplot as plt
import numpy as np
import logging
from io import BytesIO

# Configurando o logger
logger = logging.getLogger(__name__)

def home(request):
    return render(request, 'exoplanets_app/home/home.html')

def listar_objetos(request):
    return render(request, 'exoplanets_app/mid/sistemas.html')


def detection_methods(request):
    return render(request, 'exoplanets_app/mid/detection_methods.html')



def lightcurve_analysis(request):
    if request.method == 'POST':
        kepler_id = None
        pixelfile = None
        lc = None
        lc_subsampled = None
        period = None
        folded_lc = None

        kepler_id = request.POST.get('kepler_id')
        
        if not kepler_id:
            return JsonResponse({'error': 'Kepler ID is required.'}, status=400)

        try:
            # Buscar arquivos de pixels para o Kepler ID fornecido
            search_result = lk.search_targetpixelfile(kepler_id, mission='Kepler')
            
            # Verificar se existem múltiplos arquivos e, se necessário, selecionar o primeiro disponível
            if len(search_result) > 1:
                pixelfile = search_result[0].download() 
            else:
                pixelfile = search_result.download()
            
            # Verificar se o arquivo de pixels contém dados válidos
            if pixelfile is None or pixelfile.hdu[1].data.size == 0:
                return JsonResponse({'error': 'No valid data found for the provided Kepler ID.'}, status=404)
            
            # Tentar gerar a curva de luz
            try:
                lc = pixelfile.to_lightcurve(method="pld").remove_outliers().flatten()
            except Exception as e:
                return JsonResponse({'error': f'Error in light curve correction: {str(e)}'}, status=500)

            # Verificar se a curva de luz contém dados válidos
            if lc is None or lc.flux.size == 0:
                return JsonResponse({'error': 'Light curve could not be generated or contains no data.'}, status=500)

            # Subamostragem da curva de luz
            lc_subsampled = lc[::10]

            # Calcular o período e plotar a curva de luz subamostrada
            period = lc_subsampled.to_periodogram("bls").period_at_max_power
            folded_lc = lc_subsampled.fold(period)

            # Plotar e salvar o gráfico em formato base64 para exibir na web
            plt.figure(figsize=(10, 6))
            folded_lc.scatter()
            plt.title(f"Curva de luz para: {kepler_id}")
            plt.xlabel("BJD 2458679+")
            plt.ylabel("Fluxo Normalizado")
            
            # Converter o gráfico para uma string base64
            buffer = BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            image_png = buffer.getvalue()
            buffer.close()
            graphic = base64.b64encode(image_png).decode('utf-8')
            plt.close()

            return JsonResponse({
                'graphic': graphic,
                'period': str(period)
            })

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return render(request, 'exoplanets_app/mid/lightcurve_form.html')