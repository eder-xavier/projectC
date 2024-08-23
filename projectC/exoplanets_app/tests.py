from django.test import TestCase

import lightkurve as lk
import matplotlib.pyplot as plt

# Passo 1: Baixar os dados do Kepler
# Substitua 'KIC_1234567' pelo identificador do sistema desejado
kepler_id = '10544976'
search_result = lk.search_lightcurvefile(kepler_id, mission='Kepler').download_all()

# Passo 2: Carregar a curva de luz e plotar
lc = search_result.stitch().remove_nans().normalize()
lc.scatter()
plt.title(f'Curva de Luz de {kepler_id}')
plt.xlabel('Tempo')
plt.ylabel('Fluxo Normalizado')
plt.show()

# Passo 3: Estimar o período do trânsito
# Aplica a técnica de periodograma para encontrar possíveis períodos
periodogram = lc.to_periodogram(method='lombscargle')
periodogram.plot()
plt.title('Periodograma')
plt.xlabel('Período (dias)')
plt.ylabel('Poder')
plt.show()

# Passo 4: Plotar a curva de luz em fase
# Encontre o período mais forte no periodograma
best_period = periodogram.period_at_max_power
lc_folded = lc.fold(period=best_period)
lc_folded.scatter()
plt.title(f'Curva de Luz em Fase (Período = {best_period:.2f} dias)')
plt.xlabel('Fase')
plt.ylabel('Fluxo Normalizado')
plt.show()
