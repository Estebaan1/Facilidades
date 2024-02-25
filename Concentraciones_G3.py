import tkinter as tk
from PIL import Image, ImageTk

# Comentarios iniciales
comentarios_iniciales = """
Universidad Central del Ecuador
Facultad de Ingeniería en Geología, Minas, Petróleos y Ambiental
Carrera de Petróleos
Integrantes: Cuji Marco 
              Landazuri Luis 
              Quingaguano Bryan 
              Saico Esteban 
              Zhangallimbay Karen
Tema: Precio del Petróleo

Que volumen de demulsificante y biocida para un bache de 3 horas, se deben inyectar desde una plataforma que produce Qf (BFPD) 
con el %BSW de agua y en que tiempo llegará un pig, el fluido es transportado por una tubería de (Diámetro) in, una longitud L en
m, el fluido llega a una CPF.
- Concentación Biocida --> 500 ppm
- Cocentración Demulsificante --> 35 ppm
"""

# Función para realizar los cálculos
def calcular():
    # Concentraciones de biocida y demulsificante
    Cb = 500
    Cd = 35

    # Obtener los valores ingresados por el usuario desde las cajas de entrada
    Qf = float(caudal_fluido.get())
    BSW = float(porcentaje_bsw.get())
    L = float(longitud_tuberia.get())
    D = float(diametro_tuberia.get())

    # Realizar los cálculos
    Qw = Qf * (BSW / 100)
    Qo = Qf - Qw

    Vb = Qw * (3 / 24)
    x = ((Cb * Vb) / (1000000 - Cb)) * 42

    Vd = ((Cd * Qo) / (1000000 - Cd)) * 42

    L2 = L * 3.28
    Qf2 = Qf * 5.615
    D2 = D / 12
    t = ((3.1415 / 4) * (D2 ** 2) * L2) / Qf2
    t2 = t * 24

    # Mostrar los resultados en las etiquetas correspondientes
    resultado_biocida.config(text=f'El volumen de Biocida es {x:0.2f} gal/3h')
    resultado_demulsificante.config(text=f'El volumen de Demulsificante es {Vd:0.2f} gal/3h')
    resultado_tiempo.config(text=f'El tiempo de llegada al PIG es {t2:0.2f} horas')

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cálculos de Concentraciones")

# Cargar la imagen .png
imagen = Image.open("C:/Users/Pc/Desktop/Python/sello_400.png")  # Cambia "ruta/a/la/imagen.png" por la ruta de tu imagen
imagen = imagen.resize((200, 200))  # Ajusta el tamaño de la imagen si es necesario
imagen = ImageTk.PhotoImage(imagen)
etiqueta_imagen = tk.Label(ventana, image=imagen)
etiqueta_imagen.grid(row=0, column=0, columnspan=2)

# Etiqueta para los comentarios iniciales
etiqueta_comentarios = tk.Label(ventana, text=comentarios_iniciales, justify=tk.CENTER)
etiqueta_comentarios.grid(row=1, column=0, columnspan=2)

# Crear las etiquetas y cajas de entrada para los datos
tk.Label(ventana, text="Caudal del fluido (Qf) en BFPD:").grid(row=2, column=0)
caudal_fluido = tk.Entry(ventana)
caudal_fluido.grid(row=2, column=1)

tk.Label(ventana, text="%BSW en porcentaje:").grid(row=3, column=0)
porcentaje_bsw = tk.Entry(ventana)
porcentaje_bsw.grid(row=3, column=1)

tk.Label(ventana, text="Longitud de la tubería en metros (m):").grid(row=4, column=0)
longitud_tuberia = tk.Entry(ventana)
longitud_tuberia.grid(row=4, column=1)

tk.Label(ventana, text="Diámetro de la tubería en pulgadas (in):").grid(row=5, column=0)
diametro_tuberia = tk.Entry(ventana)
diametro_tuberia.grid(row=5, column=1)

# Botón para calcular
calcular_button = tk.Button(ventana, text="Calcular", command=calcular)
calcular_button.grid(row=6, column=0, columnspan=2)

# Etiquetas para mostrar los resultados
resultado_biocida = tk.Label(ventana, text="")
resultado_biocida.grid(row=7, column=0, columnspan=2)

resultado_demulsificante = tk.Label(ventana, text="")
resultado_demulsificante.grid(row=8, column=0, columnspan=2)

resultado_tiempo = tk.Label(ventana, text="")
resultado_tiempo.grid(row=9, column=0, columnspan=2)

ventana.mainloop()