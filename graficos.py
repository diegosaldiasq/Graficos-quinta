import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo de datos
file_path = './Data_logger/280125_selva_negra_turno_C_error.xlsx'   # ---------->>> Cambiar nombre de archivo excel  <<<-----------
#file_path = './Data_logger/130125_prueba_datalogger_anaconda_solo.xlsx'   # ---------->>> Cambiar nombre de archivo excel  <<<-----------
sheet_name = 'Data'
data = pd.read_excel(file_path, sheet_name=sheet_name)

# Configuración de los datos
# Convertir la columna de tiempo a formato datetime
time = pd.to_datetime(data['Time'])
# Asignar las columnas de temperatura
temp_channel_1 = data['Temperature (channel 1)']
temp_channel_2 = data['Temperature (channel 2)']

# Obtener los valores inicial y final del canal 1
first_value_channel_1 = temp_channel_1.iloc[0]
last_value_channel_1 = temp_channel_1.iloc[-1]
first_time = time.iloc[0]
last_time = time.iloc[-1]
mid_value_channel_1 = temp_channel_1.iloc[164]
mid_time = time.iloc[164]

# Crear la gráfica
plt.figure(figsize=(12, 6))
plt.plot(time, temp_channel_1, label='T° Centro térmico', marker='.')
plt.plot(time, temp_channel_2, label='T° Anaconda', marker='.')

#plt.plot(time, temp_channel_1, label='T° Sonda 1', marker='.')
#plt.plot(time, temp_channel_2, label='T° Sonda 2', marker='.')


# Añadir los valores inicial y final del canal 1 al gráfico
plt.text(first_time, first_value_channel_1, f'{first_value_channel_1}°C', color='blue', ha='right')
plt.text(last_time, last_value_channel_1, f'{last_value_channel_1}°C', color='blue', ha='left')
plt.text(mid_time, mid_value_channel_1, f'{mid_value_channel_1}°C', color='blue', ha='left')

# Configuración de los elementos del gráfico
plt.xlabel('Tiempo')
plt.ylabel('Temperatura (°C)')
plt.title('Torta selva negra SISA (de gorreri) pasada por Anaconda a 177 min 28-01-25 Turno C') # ------->>> Cambiar titulo que aparecera en el grafico <<<-----------
#plt.title('Temperatura torta mocaccino 20-01-25') # ------->>> Cambiar titulo que aparecera en el grafico <<<-----------
plt.legend()
plt.grid()
plt.tight_layout() 

# Guardar el gráfico como imagen
plt.savefig('Data_logger/Graficos/Selva negra sisa 28-01-25 turno C.png', dpi=300, bbox_inches='tight') # -------->>> Cambiar nombre de archivo que se creara <<<--------
#plt.savefig('Data_logger/Graficos/Temperatura torta mocaccino 20-01-25 jenny.png', dpi=300, bbox_inches='tight') # -------->>> Cambiar nombre de archivo que se creara <<<--------

# Mostrar el gráfico
plt.show()

#### Ejecutar como en terminal como -------->>> python graficos.py
