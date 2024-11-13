import matplotlib.pyplot as plt

# Datos para el gráfico de ejemplo
labels = ['Inversión', 'Gasto o Consumo']
sizes = [75, 25]  # Porcentajes de cada parte
colors = ['#FF6666', '#FFCC99']
explode = (0, 0.1)  # Para destacar la segunda sección

# Crear el gráfico de torta
plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, explode=explode, wedgeprops={'edgecolor': 'black'})

# Agregar el título
plt.title('Inversión y Gasto')

# Mostrar el gráfico
plt.show()
