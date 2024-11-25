import matplotlib.pyplot as plt

# Datos para las tendencias en salud digital en España y Cataluña
categories = [
    "Telemedicina",
    "Big Data en Salud",
    "Inteligencia Artificial",
    "IoT en Salud (Dispositivos Conectados)",
    "Historia Clínica Electrónica (HCE)",
    "Aplicaciones Móviles de Salud",
    "Ciberseguridad en Salud",
    "Automatización y Robótica"
]
spain_trends = [75, 70, 60, 55, 80, 65, 50, 45]  # Porcentaje de adopción o interés
catalonia_trends = [80, 72, 62, 60, 85, 70, 55, 50]

# Crear el gráfico
fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.35
x_indexes = range(len(categories))

# Graficar las barras
bars1 = ax.bar(
    [i - bar_width / 2 for i in x_indexes], spain_trends, bar_width, label="España"
)
bars2 = ax.bar(
    [i + bar_width / 2 for i in x_indexes], catalonia_trends, bar_width, label="Cataluña"
)

# Etiquetas y título
ax.set_xlabel("Tendencias", fontsize=12)
ax.set_ylabel("Nivel de Adopción (%)", fontsize=12)
ax.set_title("Evaluación del Mercado y Tendencias en Salud Digital", fontsize=14)
ax.set_xticks(x_indexes)
ax.set_xticklabels(categories, rotation=45, ha="right", fontsize=10)
ax.legend()

# Añadir valores encima de las barras
for bar_group in [bars1, bars2]:
    for bar in bar_group:
        yval = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            yval + 1,
            f"{int(yval)}%",
            ha="center",
            va="bottom",
            fontsize=9,
        )

# Ajustar diseño
plt.tight_layout()
plt.show()
