import matplotlib.pyplot as plt
import numpy as np

# Datos de los proyectos
proyectos = ['PharmaTrace Insight', 'SupportSync AI', 'SmartStock Dynamics']
presupuesto_planeado = [143500, 242000, 177000]
presupuesto_actual = [143500, 242000, 177000]  # Asumimos que es igual al planeado debido a la congelación
presupuesto_remanente = [0, 0, 0]  # Asumimos que no hay remanente debido a la congelación

# Configurar el gráfico
fig, ax = plt.subplots(figsize=(12, 6))

# Posiciones de las barras
x = np.arange(len(proyectos))
width = 0.25

# Crear las barras
rects1 = ax.bar(x - width, presupuesto_planeado, width, label='Presupuesto Planeado', color='#1f77b4')
rects2 = ax.bar(x, presupuesto_actual, width, label='Presupuesto Actual', color='#ff7f0e')
rects3 = ax.bar(x + width, presupuesto_remanente, width, label='Presupuesto Remanente', color='#2ca02c')

# Personalizar el gráfico
ax.set_ylabel('Presupuesto (€)')
ax.set_title('Dashboard de Proyectos NextIT Services')
ax.set_xticks(x)
ax.set_xticklabels(proyectos, rotation=45, ha='right')
ax.legend()

# Añadir etiquetas de valor en las barras
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'€{height:,}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 puntos de desplazamiento vertical
                    textcoords="offset points",
                    ha='center', va='bottom', rotation=90)

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

# Ajustar el diseño y mostrar
fig.tight_layout()
plt.show()
