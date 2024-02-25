# Universidad Central del Ecuador
# Facultad de Ingeniería en Geología, Minas, Petróleos y Ambiental
# Carrera de Petróleos
# Integrantes: Cuji Marco 
#              Landazuri Luis 
#              Quingaguano Bryan 
#              Saico Esteban 
#              Zhangallimbay Karen
# Tema: Precio del Petróleo

# Librerias

import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

# Ruta Completa

ruta = "C:/Users/Pc/Desktop/Python/Data_Histórica_Petróleo_2014-2024.xlsx"
data_hpet = pd.read_excel(ruta)  # Cambio en la lectura del archivo

# Matplotlib

plt.figure(figsize=(10, 6))
plt.plot(data_hpet['Fecha'], data_hpet['Último'], label='Último')
plt.plot(data_hpet['Fecha'], data_hpet['Máximo'], label='Máximo')
plt.plot(data_hpet['Fecha'], data_hpet['Mínimo'], label='Mínimo')
plt.title('Datos Históricos Petróleo [2014-2024]')
plt.xlabel('Fecha')
plt.ylabel('Precio ($)')
plt.legend()
plt.show()

# Seaborn

plt.figure(figsize=(10, 6))
sns.set(style="darkgrid")  # Estilo de Seaborn
sns.lineplot(data=data_hpet, x='Fecha', y='Último', label='Último')
sns.lineplot(data=data_hpet, x='Fecha', y='Máximo', label='Máximo')
sns.lineplot(data=data_hpet, x='Fecha', y='Mínimo', label='Mínimo') 
plt.title('Datos Históricos Petróleo [2014-2024]')
plt.xlabel('Fecha')
plt.ylabel('Precio ($)')
plt.legend()
plt.show()

# Plotly

fig2 = px.line(data_hpet, x='Fecha', y=['Último', 'Máximo', 'Mínimo'], title='Datos Históricos Petróleo [2014-2024]', labels={'Fecha': 'Fecha', 'value': 'Precio'})

fig2.update_layout(xaxis_title='Fecha', yaxis_title='Precio ($)')
fig2.show()

# Bokeh

from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource  # noqa: E402
from datetime import datetime

# Convertir la columna 'Fecha' a tipo datetime

data_hpet['Fecha'] = pd.to_datetime(data_hpet['Fecha'])

# Definir la salida del archivo HTML

output_file("grafico_precio_petroleo.html")

# Crear una fuente de datos

source = ColumnDataSource(data_hpet)

# Crear la figura

p = figure(title="Datos Históricos Petróleo [2014-2024]", x_axis_label='Fecha', y_axis_label='Precio ($)')

# Graficar líneas

p.line(x='Fecha', y='Último', line_width=2, legend_label='Último', color='blue', source=source)
p.line(x='Fecha', y='Máximo', line_width=2, legend_label='Máximo', color='green', source=source)
p.line(x='Fecha', y='Mínimo', line_width=2, legend_label='Mínimo', color='red', source=source)

# Mostrar la leyenda

p.legend.location = "top_left"

# Mostrar la figura

show(p) # type: ignore