import base64
from io import BytesIO
import logging
import lightkurve as lk
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from django.shortcuts import render
from scipy.signal import find_peaks
from astropy.timeseries import LombScargle


logger = logging.getLogger(__name__)

def home(request):
    return render(request, 'exoplanets_app/home/home.html')

def listar_objetos(request):
    return render(request, 'exoplanets_app/mid/sistemas.html')

def estimate_period(time_data, flux_data):
    frequency, power = LombScargle(time_data, flux_data).autopower()
    best_frequency = frequency[np.argmax(power)]
    period = 1 / best_frequency
    return period


def analyze_ttv(eclipses):
    if len(eclipses) < 2:
        return {
            'eclipses': len(eclipses),
            'expected_intervals': None,
            'observed_intervals': [],
            'ttv': [],
        }

    intervals = np.diff(eclipses)
    expected_intervals = np.mean(intervals)
    ttv = intervals - expected_intervals
    return {
        'eclipses': len(eclipses),
        'expected_intervals': expected_intervals,
        'observed_intervals': intervals,
        'ttv': ttv,
    }

def detect_eclipses(time_data, flux_data):
    eclipses = []
    threshold = 0.98
    for i in range(1, len(flux_data) - 1):
        if flux_data[i] < threshold and flux_data[i] < flux_data[i-1] and flux_data[i] < flux_data[i+1]:
            eclipses.append(time_data[i])
    return eclipses



def generate_light_curve_plot(time, flux):
    if np.isnan(time).any() or np.isinf(time).any():
        logger.error("Dados de tempo inválidos para o gráfico.")
        return None

    if np.isnan(flux).any() or np.isinf(flux).any():
        logger.error("Dados de fluxo inválidos para o gráfico.")
        return None

    plt.figure(figsize=(6, 4))
    plt.plot(time, flux, 'r.')
    plt.xlabel("Tempo (dias)")
    plt.ylabel("Fluxo Normalizado")
    plt.title("Curva de Luz Normalizada")
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    graphic = base64.b64encode(buffer.read()).decode('utf-8')
    buffer.close()
    plt.close()
    return graphic

def generate_oc_diagram(eclipses, expected_interval):
    if not eclipses or expected_interval is None:
        logger.error("Eclipses ou intervalo esperado inválidos para o diagrama O-C.")
        return None

    oc_values = [(e - (eclipses[0] + i * expected_interval)) for i, e in enumerate(eclipses)]
    plt.figure(figsize=(6, 4))
    plt.plot(range(len(oc_values)), oc_values, 'bo-', markersize=3, linewidth=2)
    plt.xlabel("Número de Eclipse")
    plt.ylabel("O-C (Dias)")
    plt.title("Diagrama O-C")

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    oc_diagram = base64.b64encode(buffer.read()).decode('utf-8')
    buffer.close()
    plt.close()
    return oc_diagram



logger = logging.getLogger(__name__)


def analyze_ltt(eclipses, period):
    if len(eclipses) < 2:
        return {
            'eclipses': len(eclipses),
            'expected_intervals': None,
            'observed_intervals': [],
            'ltt': [],
        }

    # Verifica se o período fornecido é válido
    if period <= 0:
        raise ValueError("O período deve ser um valor positivo.")

    # Calcula os intervalos observados entre os eclipses
    intervals = np.diff(eclipses)
    
    # O intervalo esperado é o período fornecido
    expected_interval = period
    
    # Calcula as variações no tempo de chegada dos eclipses (LTT)
    ltt = intervals - expected_interval

    return {
        'eclipses': len(eclipses),
        'expected_intervals': expected_interval,
        'observed_intervals': intervals,
        'ltt': ltt,
    }


def generate_phase_curve(light_curve, period):
    try:
        logger.info(f"Recebido para gerar curva de luz em fase: Período = {period}")
        
        if period <= 0:
            raise ValueError("O período deve ser um valor positivo.")

        phase = (light_curve.time.value % period) / period

        plt.figure(figsize=(10, 6))
        plt.scatter(phase, light_curve.flux.value, s=1, alpha=0.5)
        plt.xlabel('Fase')
        plt.ylabel('Fluxo Normalizado')
        plt.title('Curva de Luz em Fase')
        plt.grid(True)

        buf = BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        phase_curve = base64.b64encode(buf.getvalue()).decode('utf-8')
        buf.close()
        plt.close()

        logger.info("Curva de luz em fase gerada com sucesso.")
        return phase_curve
    except Exception as e:
        logger.error(f"Erro ao gerar a curva de luz em fase: {e}")
        return None
    


def analisar_curvas(request):
    identifier = request.GET.get('identifier', '')
    graphic = None
    phase_curve_graphic = None
    ltt_results = None
    oc_diagram = None
    period = None
    search_result = None

    if identifier:
        try:
            search_result = lk.search_lightcurve(f'{identifier}', mission='kepler').download_all()
            light_curve = search_result.stitch().remove_nans()

            if np.any(np.isnan(light_curve.time.value)) or np.any(np.isnan(light_curve.flux.value)):
                raise ValueError("Dados da curva de luz contêm valores NaN.")

            if np.any(np.isinf(light_curve.time.value)) or np.any(np.isinf(light_curve.flux.value)):
                raise ValueError("Dados da curva de luz contêm valores infinitos.")

            light_curve = light_curve.normalize()
            time_data = light_curve.time.value
            flux_data = light_curve.flux.value

            graphic = generate_light_curve_plot(time_data, flux_data)

            if request.method == 'POST':
                try:
                    period_str = request.POST.get('period', '').strip()
                    logger.info(f"Valor recebido do período: '{period_str}'")

                    if period_str:
                        period = float(period_str)
                        if period <= 0:
                            raise ValueError("O período deve ser um valor positivo.")

                        if request.POST.get('generate_phase_curve'):
                            logger.info(f"Iniciando geração da curva de luz em fase.")
                            phase_curve_graphic = generate_phase_curve(light_curve, period)

                        if request.POST.get('generate_ltt'):
                            eclipses = detect_eclipses(np.array(time_data), np.array(flux_data))
                            ltt_results = analyze_ltt(eclipses, period)
                            oc_diagram = generate_oc_diagram(eclipses, ltt_results['expected_intervals'])

                except ValueError as ve:
                    logger.error(f"Valor do período inválido: {ve}")
                    return render(request, 'exoplanets_app/mid/analisar_curvas.html', {
                        'error_message': str(ve),
                        'identifier': identifier,
                        'graphic': graphic,
                        'phase_curve_graphic': phase_curve_graphic,
                        'ltt_results': ltt_results,
                        'oc_diagram': oc_diagram,
                        'period': period,
                    })

        except Exception as e:
            error_message = f"Erro ao buscar ou processar os dados: {str(e)}"
            return render(request, 'exoplanets_app/mid/analisar_curvas.html', {
                'error_message': error_message,
                'identifier': identifier,
            })

    return render(request, 'exoplanets_app/mid/analisar_curvas.html', {
        'search_result': search_result if identifier else None,
        'graphic': graphic,
        'phase_curve_graphic': phase_curve_graphic,
        'identifier': identifier,
        'ltt_results': ltt_results,
        'oc_diagram': oc_diagram,
        'period': period,
    })



