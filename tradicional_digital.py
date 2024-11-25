import matplotlib.pyplot as plt
import numpy as np

# Datos ficticios para replicar el gráfico
time = np.linspace(0, 10, 100)  # Tiempo (0 a 10 años)
performance_traditional = np.piecewise(
    time,
    [time < 2, (time >= 2) & (time < 6), time >= 6],
    [lambda x: 0.8 - 0.3 * x, lambda x: 0.3 + 0.1 * (x - 2), lambda x: 0.7 + 0.2 * (x - 6)],
)
performance_digital = 0.6 + 0.4 * np.sin(0.5 * np.pi * time / 2) + 0.1 * time

# Crear el gráfico
plt.figure(figsize=(12, 6))
plt.plot(time, performance_traditional, label="Economía Tradicional", linestyle="--", color="blue")
plt.plot(time, performance_digital, label="Economía Digital", color="green")

# Añadir etiquetas y título
plt.title("Impacto de la Transformación Digital en Cataluña", fontsize=14)
plt.xlabel("Tiempo (Años)", fontsize=12)
plt.ylabel("Desempeño (Indicador de Eficiencia)", fontsize=12)

# Anotaciones para resaltar puntos clave
plt.axvline(x=2, color="gray", linestyle=":", label="Inicio del Cambio")
plt.text(2, 0.6, "Inicio del cambio", color="gray", fontsize=10, rotation=90, ha="right")

# Líneas adicionales para los ejes de referencia
plt.axhline(y=0.8, color="black", linestyle=":", linewidth=0.8)
plt.axhline(y=1.0, color="black", linestyle=":", linewidth=0.8)

# Etiquetas para economía digital
plt.annotate(
    "Progreso rápido\ngracias a la agilidad",
    xy=(8, performance_digital[80]),
    xytext=(6, 1.2),
    arrowprops=dict(facecolor="black", arrowstyle="->"),
    fontsize=10,
)

# Etiquetas para economía tradicional
plt.annotate(
    "Recuperación lenta\ny mejora limitada",
    xy=(8, performance_traditional[80]),
    xytext=(6, 0.6),
    arrowprops=dict(facecolor="black", arrowstyle="->"),
    fontsize=10,
)

# Añadir leyenda
plt.legend(fontsize=10)
plt.grid(alpha=0.3)
plt.tight_layout()

# Mostrar el gráfico
plt.show()
