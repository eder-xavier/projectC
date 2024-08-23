from django.shortcuts import render
from django.http import JsonResponse
import lightkurve as lk
import io
import base64
import matplotlib.pyplot as plt
import numpy as np
import logging
import time  # Para simular o tempo de processamento

# Configurando o logger
logger = logging.getLogger(__name__)

def home(request):
    return render(request, 'exoplanets_app/home/home.html')

def listar_objetos(request):
    return render(request, 'exoplanets_app/mid/sistemas.html')

def exoplanet_discovery(request):
    return render(request, 'exoplanets_app/mid/exoplanet_discovery.html')

def generate_lightcurve(request):
    if request.method == 'POST':
        kepler_id = request.POST.get('kepler_id')
        logger.info(f"Identificador Kepler recebido: {kepler_id}")  # Log para verificar o valor do identificador

        if not kepler_id:
            logger.error("Identificador Kepler não foi fornecido.")
            return JsonResponse({'error': 'Por favor, forneça um identificador Kepler válido.'})

        try:
            logger.info("Iniciando a busca pela curva de luz...")
            search_result = lk.search_lightcurve(f'KIC {kepler_id}', mission='Kepler')
            logger.info(f"Resultados da busca: {search_result}")

            if len(search_result) == 0:
                logger.error("Nenhum dado encontrado para o identificador Kepler fornecido.")
                return JsonResponse({'error': 'Nenhum dado encontrado para o identificador Kepler fornecido.'})

            logger.info("Baixando e processando os dados da curva de luz...")
            lc = search_result.download_all().stitch().remove_nans().remove_outliers()
            flat_lc = lc.flatten()
            lightcurve_plot = plot_to_base64(flat_lc)
            request.session['flat_lc'] = flat_lc.to_table().as_array().tolist()

            logger.info("Curva de luz gerada com sucesso.")
            return JsonResponse({'lightcurve_plot': lightcurve_plot})
        except Exception as e:
            logger.exception("Erro ao processar a curva de luz.")
            return JsonResponse({'error': f'Ocorreu um erro ao processar os dados: {str(e)}'})

def estimate_period(request):
    if request.method == 'POST':
        try:
            logger.info("Iniciando a estimativa do período...")
            flat_lc_data = request.session['flat_lc']
            flat_lc = lk.LightCurve(data=flat_lc_data)

            periodogram = flat_lc.to_periodogram(method="bls", period=np.linspace(0.5, 30, 10000))
            best_period = periodogram.period_at_max_power
            periodogram_plot = plot_to_base64(periodogram)
            request.session['best_period'] = best_period.value

            logger.info(f"Período estimado: {best_period.value} dias")
            return JsonResponse({'periodogram_plot': periodogram_plot, 'best_period': round(best_period.value, 4)})
        except Exception as e:
            logger.exception("Erro ao estimar o período.")
            return JsonResponse({'error': f'Ocorreu um erro ao processar os dados: {str(e)}'})

def identify_exoplanet(request):
    if request.method == 'POST':
        try:
            logger.info("Iniciando a identificação do exoplaneta...")
            flat_lc_data = request.session['flat_lc']
            flat_lc = lk.LightCurve(data=flat_lc_data)
            best_period = request.session['best_period']

            folded_lc = flat_lc.fold(period=best_period)
            folded_lightcurve_plot = plot_to_base64(folded_lc)

            logger.info("Curva de luz dobrada gerada com sucesso.")
            return JsonResponse({'folded_lightcurve_plot': folded_lightcurve_plot})
        except Exception as e:
            logger.exception("Erro ao identificar o exoplaneta.")
            return JsonResponse({'error': f'Ocorreu um erro ao processar os dados: {str(e)}'})

def plot_to_base64(plot_data):
    logger.info("Gerando gráfico em base64...")
    buffer = io.BytesIO()
    plot_data.plot()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png).decode('utf-8')
    logger.info("Gráfico gerado com sucesso.")
    return graphic
