import os
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog, messagebox

# Configurar Tkinter (para la selección de archivos)
root = tk.Tk()
root.withdraw()  # Oculta la ventana principal

# Pedir al usuario que seleccione el archivo Excel
file_path = filedialog.askopenfilename(
    title="Seleccionar archivo Excel",
    filetypes=[("Archivos Excel", "*.xlsx")]
)

# Si no se selecciona un archivo, mostrar un mensaje de error y salir
if not file_path:
    messagebox.showerror("Error", "No seleccionaste ningún archivo.")
    exit()

# Cargar el archivo de datos
sheet_name = "Data"
data = pd.read_excel(file_path, sheet_name=sheet_name)

# Convertir la columna de tiempo a formato datetime
time = pd.to_datetime(data["Time"])
temp_channel_1 = data["Temperature (channel 1)"]
temp_channel_2 = data["Temperature (channel 2)"]

# Obtener valores inicial, intermedio y final del canal 1
first_value_channel_1 = temp_channel_1.iloc[0]
last_value_channel_1 = temp_channel_1.iloc[-1]
first_time = time.iloc[0]
last_time = time.iloc[-1]
mid_value_channel_1 = temp_channel_1.iloc[164]
mid_time = time.iloc[164]

# Crear la carpeta de salida si no existe
output_folder = os.path.join(os.path.dirname(file_path), "Graficos")
os.makedirs(output_folder, exist_ok=True)

# Nombre del archivo de salida basado en el archivo Excel
output_filename = os.path.join(output_folder, f"Grafico_{os.path.basename(file_path).replace('.xlsx', '.png')}")

# Crear la gráfica
plt.figure(figsize=(12, 6))
plt.plot(time, temp_channel_1, label="T° Centro térmico", marker=".")
plt.plot(time, temp_channel_2, label="T° Anaconda", marker=".")

# Anotaciones de valores clave
plt.text(first_time, first_value_channel_1, f"{first_value_channel_1}°C", color="blue", ha="right")
plt.text(last_time, last_value_channel_1, f"{last_value_channel_1}°C", color="blue", ha="left")
plt.text(mid_time, mid_value_channel_1, f"{mid_value_channel_1}°C", color="blue", ha="left")

# Configuración del gráfico
plt.xlabel("Tiempo")
plt.ylabel("Temperatura (°C)")
plt.title(f"Gráfico generado para {os.path.basename(file_path)}")
plt.legend()
plt.grid()
plt.tight_layout()

# Guardar la imagen
plt.savefig(output_filename, dpi=300, bbox_inches="tight")

# Mostrar mensaje de éxito
messagebox.showinfo("Éxito", f"Gráfico guardado en:\n{output_filename}")

# Mostrar el gráfico
plt.show()
