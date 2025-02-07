import matplotlib.pyplot as plt
import numpy as np

# Datos actualizados de proyectos
proyectos = [
    'AI-Driven Customer Analytics',
    'Cybersecurity Framework v2.0',
    'IoT Supply Chain Monitoring',
    'Cloud Migration Accelerator',
    'Automated Compliance System',
    'Predictive Maintenance Platform'
]

presupuesto = [150000, 250000, 120000, 300000, 150000, 230000]  # En euros
roi = [22, 35, 18, 28, 40, 25]  # Porcentaje
recursos = [6, 5, 5, 7, 4, 6]  # Personas asignadas
riesgo = ['Alto', 'Moderado', 'Moderado-Alto', 'Bajo', 'Bajo-Moderado', 'Moderado']

# Configurar figura y ejes
fig, ax1 = plt.subplots(figsize=(14, 8))

# Barras para presupuesto
bars = ax1.bar(proyectos, presupuesto, color='#1f77b4', alpha=0.7)
ax1.set_ylabel('Presupuesto (€)', color='#1f77b4')
ax1.tick_params(axis='y', labelcolor='#1f77b4')
ax1.set_xticklabels(proyectos, rotation=45, ha='right')

# Segundo eje para ROI
ax2 = ax1.twinx()
line = ax2.plot(proyectos, roi, color='#ff7f0e', marker='o', linewidth=2, markersize=8)
ax2.set_ylabel('ROI Esperado (%)', color='#ff7f0e')
ax2.tick_params(axis='y', labelcolor='#ff7f0e')
ax2.set_ylim(0, 50)

# Añadir etiquetas
ax1.set_title('Portfolio de Proyectos NextIT Services \n(Facturación Anual: €12M)')

# Leyenda combinada
lines = [plt.Line2D([0], [0], color='#1f77b4', lw=4),
         plt.Line2D([0], [0], color='#ff7f0e', marker='o', linestyle='')]
labels = ['Presupuesto', 'ROI Esperado']
plt.legend(lines, labels, loc='upper left')

# Añadir valores en barras
for bar, valor in zip(bars, presupuesto):
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height,
             f'€{valor:,}',
             ha='center', va='bottom', rotation=90)

# Añadir valores de ROI
for x, y in zip(proyectos, roi):
    ax2.text(x, y+1, f'{y}%', ha='center', color='#ff7f0e', fontweight='bold')

plt.tight_layout()
plt.show()
