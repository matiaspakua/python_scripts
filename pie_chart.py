import matplotlib.pyplot as plt

# Datos para el gráfico de ejemplo
labels = ['Inversión', 'Gasto o Consumo']
sizes = [75, 25]  # Porcentajes de cada parte
colors = ['#FF6666', '#FFCC99']
explode = (0, 0.1)  # Para destacar la segunda sección

# Crear el gráfico de torta
plt.figure(figsize=(8, 8))
wedges, texts, autotexts = plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, explode=explode, wedgeprops={'edgecolor': 'black'})

# Agregar el título
plt.title('Inversión y Gasto')

# Agregar una leyenda
plt.legend(wedges, labels, title="Categorías", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Mejorar la visualización de los textos
for text in autotexts:
    text.set_color('white')
    text.set_fontsize(12)

# Guardar el gráfico en un archivo
plt.savefig('inversion_gasto_pie_chart.png', bbox_inches='tight')

# Mostrar el gráfico
plt.show()
