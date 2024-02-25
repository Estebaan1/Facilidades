# Universidad Central del Ecuador
# Facultad de Ingeniería en Geología, Minas, Petróleos y Ambiental
# Carrera de Petróleos
# Integrantes: Cuji Marco 
#              Landazuri Luis 
#              Quingaguano Bryan 
#              Saico Esteban 
#              Zhangallimbay Karen
# Tema: Ley de Stokes

import math
import tkinter as tk
from PIL import Image, ImageTk

def calcular():
    bfpd = float(caudal_fluido.get())
    bwpd = float(caudal_agua.get())
    gravedad_api = float(gravedad.get())
    pae = float(porcentaje_agua_emulsionada.get())
    viscosidad_petroleo = float(viscosidad.get())
    va = float(velocidad_asentamiento.get())
    
    bopd=bfpd-bwpd
    emulsion=(bopd*100)/(100-pae)
    AE=emulsion-bopd
    AL=bwpd-AE
    
    da=1
    drp=141.5/(131.5+gravedad_api)
    dp=drp*da
    
    d = math.sqrt((va * viscosidad_petroleo) / ((1.072 * 10**-4) * (da - dp)))
    
    resultado_text.set(f"El caudal del petróleo es {bopd:0.2f} BOPD.\n"
                       f"La emulsión es {emulsion:0.2f} bbl.\n"
                       f"Agua Emulsionada {AE:0.2f} bbl.\n"
                       f"Agua Libre {AL:0.2f} bbl.\n"
                       f"El diámetro de la gota de agua en la emulsión es aproximadamente {d:0.2f} µm.")

# Crear la ventana principal
root = tk.Tk()
root.title("Cálculo de Ley de Stokes")

# Cargar la imagen .png
imagen = Image.open("C:/Users/Pc/Desktop/Python/sello_400.png")
imagen = imagen.resize((50, 50))  # Ajusta el tamaño de la imagen si es necesario
imagen = ImageTk.PhotoImage(imagen)
etiqueta_imagen = tk.Label(root, image=imagen)
etiqueta_imagen.grid(row=0, column=0, columnspan=2)

# Crear los widgets
tk.Label(root, text="Caudal del fluido (BFPD):").grid(row=1, column=0)
caudal_fluido = tk.Entry(root)
caudal_fluido.grid(row=1, column=1)

tk.Label(root, text="Caudal de agua (BWPD):").grid(row=2, column=0)
caudal_agua = tk.Entry(root)
caudal_agua.grid(row=2, column=1)

tk.Label(root, text="Gravedad API del petróleo:").grid(row=3, column=0)
gravedad = tk.Entry(root)
gravedad.grid(row=3, column=1)

tk.Label(root, text="Porcentaje de agua emulsionada (%):").grid(row=4, column=0)
porcentaje_agua_emulsionada = tk.Entry(root)
porcentaje_agua_emulsionada.grid(row=4, column=1)

tk.Label(root, text="Viscosidad del petróleo (cP):").grid(row=5, column=0)
viscosidad = tk.Entry(root)
viscosidad.grid(row=5, column=1)

tk.Label(root, text="Velocidad de asentamiento de la gota (ft/min):").grid(row=6, column=0)
velocidad_asentamiento = tk.Entry(root)
velocidad_asentamiento.grid(row=6, column=1)

calcular_button = tk.Button(root, text="Calcular", command=calcular)
calcular_button.grid(row=7, column=0, columnspan=2)

resultado_text = tk.StringVar()
resultado_label = tk.Label(root, textvariable=resultado_text)
resultado_label.grid(row=8, column=0, columnspan=2)

# Ejecutar el bucle principal
root.mainloop()