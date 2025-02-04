import matplotlib.pyplot as plt
import numpy as np

# Datos actualizados con aumento de 100,000€ por proyecto
proyectos = [
    'AI-Driven Customer Analytics',
    'Cybersecurity Framework v2.0',
    'IoT Supply Chain Monitoring',
    'Cloud Migration Accelerator',
    'Automated Compliance System',
    'Predictive Maintenance Platform'
]

presupuesto_planeado = [250000, 350000, 220000, 400000, 250000, 330000]  # +100,000€ cada uno
presupuesto_actual = [132000, 165000, 98000, 180000, 120000, 150000]
presupuesto_remanente = [118000, 185000, 122000, 220000, 130000, 180000]

# Configurar el gráfico
fig, ax = plt.subplots(figsize=(16, 8))

# Posiciones de las barras
x = np.arange(len(proyectos))
width = 0.6

# Crear las barras apiladas
ax.bar(x, presupuesto_actual, width, label='Presupuesto Actual', color='#FF6F61')
ax.bar(x, presupuesto_remanente, width, bottom=presupuesto_actual, label='Presupuesto Remanente', color='#6B5B95')

# Añadir línea de presupuesto planeado
ax.plot(x, presupuesto_planeado, 'D', color='#88B04B', markersize=12, label='Presupuesto Planeado')

# Personalización avanzada
ax.set_ylabel('Presupuesto (€)', fontsize=12, fontweight='bold')
ax.set_title('Estado Presupuestario Proyectos NextIT - Feb 2025\n', 
             fontsize=14, fontweight='bold', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(proyectos, rotation=45, ha='right', fontsize=10)
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_axisbelow(True)

# Añadir etiquetas de valores
for i, (act, rem, pla) in enumerate(zip(presupuesto_actual, presupuesto_remanente, presupuesto_planeado)):
    ax.text(i, act/2, f'€{act/1000:.0f}K', ha='center', va='center', color='white', fontsize=9)
    ax.text(i, act + rem/2, f'€{rem/1000:.0f}K', ha='center', va='center', color='white', fontsize=9)
    ax.text(i, pla+5000, f'€{pla/1000:.0f}K', ha='center', va='bottom', color='#88B04B', fontsize=10)

# Leyenda mejorada
ax.legend(loc='upper right', framealpha=0.95, shadow=True)

plt.tight_layout()
plt.show()
