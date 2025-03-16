import matplotlib.pyplot as plt
import numpy as np

# Datos del mercado SaaS en España (en millones de euros)
years = [2025, 2026]
saas_market = [8160, 9700]  # Mercado SaaS (millones de euros)
automation_adoption = [85, 90]  # Adopción de automatización en atención al cliente (%)

# Crear el gráfico
fig, ax1 = plt.subplots()

# Gráfico del mercado SaaS
color = 'tab:blue'
ax1.set_xlabel('Año')
ax1.set_ylabel('Mercado SaaS (millones de euros)', color=color)
ax1.bar(years, saas_market, color=color, alpha=0.7, label='Mercado SaaS')
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_ylim(0, 11000)

# Añadir una segunda escala para la adopción de automatización
ax2 = ax1.twinx()
color = 'tab:green'
ax2.set_ylabel('Adopción de Automatización (%)', color=color)
ax2.plot(years, automation_adoption, color=color, marker='o', linestyle='--', linewidth=2, label='Adopción de Automatización')
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_ylim(0, 100)

# Títulos y leyendas
fig.suptitle('Proyección del Mercado SaaS y Automatización en España (2025-2026)', fontsize=14)
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Mostrar el gráfico
plt.tight_layout()
plt.show()
