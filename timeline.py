import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Datos
proyectos = [
    "AI-Driven Customer Analytics",
    "IoT Supply Chain Monitoring",
    "Cybersecurity Framework v2.0",
    "Automated Compliance System",
    "Predictive Maintenance Platform",
    "Cloud Migration Accelerator",
    "PharmaTrace Insight",
    "SupportSync AI",
    "SmartStock Dynamics"
]

# Fechas de inicio y fin de los proyectos
fechas_inicio = [
    "2024-01-01", "2024-04-01", "2024-01-01",
    "2024-02-01", "2024-07-01",
    "2024-01-01", "2025-03-01",
    "2025-04-01", "2025-01-01"
]

fechas_fin = [
    "2025-03-31", "2025-06-30", "2025-09-30",
    "2025-05-31", "2025-12-31",
    "2025-04-30", "2025-04-30",
    "2025-06-30", "2025-12-31"
]

# Convertir fechas a objetos datetime
fechas_inicio = [datetime.strptime(fecha, "%Y-%m-%d") for fecha in fechas_inicio]
fechas_fin = [datetime.strptime(fecha, "%Y-%m-%d") for fecha in fechas_fin]

# Crear el gráfico
fig, ax = plt.subplots(figsize=(14, 8))

# Crear barras horizontales
for i, proyecto in enumerate(proyectos):
    color = 'skyblue' if proyecto != "PharmaTrace Insight" else 'lightgray'
    ax.barh(proyecto, (fechas_fin[i] - fechas_inicio[i]).days, left=fechas_inicio[i], color=color)

# Configurar etiquetas y título
ax.set_title("Diagrama de Gantt - Proyectos NextEra IT (2025)", fontsize=16)
ax.set_xlabel("Fecha", fontsize=12)
ax.set_ylabel("Proyectos", fontsize=12)

# Formatear ejes
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
