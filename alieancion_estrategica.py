import re
import matplotlib.pyplot as plt
import numpy as np

# Configuración de datos
proyectos = {
    # Proyectos en curso (Gris)
    'SmartStock Dynamics': {'impacto': 7, 'viabilidad': 7, 'roi': 25, 'color': '#CCCCCC'},
    'Cybersecurity v2.0': {'impacto': 9, 'viabilidad': 8, 'roi': 35, 'color': '#CCCCCC'},
    'Cloud Migrator': {'impacto': 6, 'viabilidad': 9, 'roi': 28, 'color': '#CCCCCC'},
    'Data Lake Expansion': {'impacto': 8, 'viabilidad': 7, 'roi': 30, 'color': '#CCCCCC'},
    'Legacy System Upgrade': {'impacto': 6, 'viabilidad': 8, 'roi': 22, 'color': '#CCCCCC'},

    # Nuevos Proyectos (Colores vibrantes)
    'AutoScale CX': {'impacto': 10, 'viabilidad': 9, 'roi': 40, 'color': '#2ECC71'},
    'AI Compliance': {'impacto': 9, 'viabilidad': 8, 'roi': 35, 'color': '#F39C12'}
}

# Preparar datos para el gráfico
impacto = [p['impacto'] for p in proyectos.values()]
viabilidad = [p['viabilidad'] for p in proyectos.values()]
roi = [p['roi']*40 for p in proyectos.values()]  # Escalar ROI para tamaño burbuja
colores = [p['color'] for p in proyectos.values()]
etiquetas = list(proyectos.keys())

# Crear gráfico
plt.figure(figsize=(14, 10))
scatter = plt.scatter(viabilidad, impacto, s=roi, c=colores, alpha=0.7, edgecolors='black')

# Añadir etiquetas
for i, txt in enumerate(etiquetas):
    plt.annotate(txt, (viabilidad[i]+0.1, impacto[i]), 
                 fontsize=9, ha='left', va='center')

# Línea de ROI mínimo estratégico
plt.axhline(y=7.5, color='#3498DB', linestyle='--', linewidth=1)
plt.text(x=5.5, y=7.7, s='ROI Mínimo Estratégico (25%)', color='#3498DB', fontsize=10)

# Personalización
plt.title('Matriz de Priorización Estratégica NextIT - Feb 2025', fontsize=16, pad=20)
plt.xlabel('Viabilidad Operativa →', fontsize=12)
plt.ylabel('← Impacto Estratégico', fontsize=12)
plt.xlim(4, 10)
plt.ylim(5, 11)

# Leyenda de tamaño (ROI)
handles, labels = scatter.legend_elements(prop="sizes", alpha=0.6, num=4)

# Extraer números de las etiquetas y convertirlos a porcentajes
legend_roi = plt.legend(handles, [f'{int(re.search(r"\d+", l).group()) // 40}%' for l in labels],
                        title="ROI (%)", loc='lower left', bbox_to_anchor=(0.15, 0.05))

# Leyenda de colores
legend_elements = [
    plt.Line2D([0], [0], marker='o', color='w', label='Proyectos Actuales',
               markerfacecolor='#CCCCCC', markersize=10),
    plt.Line2D([0], [0], marker='o', color='w', label='AutoScale CX (Prioridad 1)',
               markerfacecolor='#2ECC71', markersize=10),
    plt.Line2D([0], [0], marker='o', color='w', label='AI Compliance (Prioridad 2)',
               markerfacecolor='#F39C12', markersize=10)
]

plt.legend(handles=legend_elements, loc='upper right', 
           title="Leyenda de Proyectos", frameon=True)

plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
