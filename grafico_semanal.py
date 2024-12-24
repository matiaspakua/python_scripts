import matplotlib.pyplot as plt
import pandas as pd

# Datos iniciales: puedes empezar con datos en blanco o algunos valores de ejemplo.
data = {
    "Semana": [],
    "Publicaciones": [],
    "Reacciones": []
}

def ingresar_datos():
    """Función para ingresar los datos semanalmente."""
    semana = input("Ingresa el nombre o número de la semana: ")
    publicaciones = int(input(f"Cantidad de publicaciones para {semana}: "))
    reacciones = int(input(f"Cantidad de reacciones para {semana}: "))

    # Agregar datos al diccionario
    data["Semana"].append(semana)
    data["Publicaciones"].append(publicaciones)
    data["Reacciones"].append(reacciones)

def generar_grafico():
    """Función para generar el gráfico dinámico."""
    df = pd.DataFrame(data)  # Convertir los datos a un DataFrame

    # Crear el gráfico de barras
    x = df["Semana"]
    width = 0.4  # Ancho de las barras

    fig, ax = plt.subplots(figsize=(10, 6))

    # Barras para Publicaciones
    ax.bar(x, df["Publicaciones"], width, label="Publicaciones", alpha=0.7)

    # Barras para Reacciones (desplazadas ligeramente para no superponerse)
    ax.bar(x, df["Reacciones"], width, label="Reacciones", alpha=0.7, bottom=df["Publicaciones"])

    # Etiquetas y diseño
    ax.set_xlabel("Semanas")
    ax.set_ylabel("Cantidad")
    ax.set_title("Publicaciones y Reacciones por Semana")
    ax.legend()

    # Mostrar el gráfico
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Ejecución principal
while True:
    print("\n--- Actualización Semanal ---")
    ingresar_datos()
    generar_grafico()

    continuar = input("¿Quieres ingresar otra semana? (s/n): ").lower()
    if continuar != 's':
        break

print("Programa finalizado. Gracias por usar la herramienta.")
