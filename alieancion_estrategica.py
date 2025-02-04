import matplotlib.pyplot as plt

# Datos de los proyectos
proyectos = ['PharmaTrace Insight', 'SupportSync AI', 'SmartStock Dynamics']
impacto = [8, 9, 7]
viabilidad = [6, 5, 7]  # Estimado basado en la información proporcionada
roi = [22, 35, 18]

# Crear el gráfico de burbujas
fig, ax = plt.subplots(figsize=(10, 8))

scatter = ax.scatter(viabilidad, impacto, s=[r*20 for r in roi], alpha=0.5, 
                     c=['#FF9999', '#66B2FF', '#99FF99'])

# Añadir etiquetas para cada burbuja
for i, proyecto in enumerate(proyectos):
    ax.annotate(proyecto, (viabilidad[i], impacto[i]), 
                xytext=(5, 5), textcoords='offset points')

# Personalizar el gráfico
ax.set_xlabel('Viabilidad', fontsize=12)
ax.set_ylabel('Impacto Estratégico', fontsize=12)
ax.set_title('Matriz de Priorización de Proyectos NextIT Services', fontsize=14)
ax.grid(True, linestyle='--', alpha=0.7)

# Añadir una leyenda para el tamaño de las burbujas
handles, labels = scatter.legend_elements(prop="sizes", alpha=0.5, 
                                          func=lambda s: s/20, num=3)
legend = ax.legend(handles, labels, loc="upper left", title="ROI (%)")

plt.tight_layout()
plt.show()
