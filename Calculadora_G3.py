# Universidad Central del Ecuador
# Facultad de Ingeniería en Geología, Minas, Petróleos y Ambiental
# Carrera de Petróleos
# Integrantes: Cuji Marco 
#              Landazuri Luis 
#              Quingaguano Bryan 
#              Saico Esteban 
#              Zhangallimbay Karen
# Tema: Calculadora Petrolera

import tkinter as tk

def convertir_volumen(valor, desde_unidad, hacia_unidad):
    factores_de_conversion = {
        "m3": 1,
        "ft3": 0.0283168,
        "gal": 0.00378541,
        "L": 0.001
    }
    return valor * factores_de_conversion[desde_unidad] / factores_de_conversion[hacia_unidad]

def convertir_tasa_de_flujo(valor, desde_unidad, hacia_unidad):
    factores_de_conversion = {
        "m3/s": 1,
        "ft3/min": 4.719474432e-5,
        "L/s": 0.001
    }
    return valor * factores_de_conversion[desde_unidad] / factores_de_conversion[hacia_unidad]

def convertir_densidad(valor, desde_unidad, hacia_unidad):
    factores_de_conversion = {
        "kg/m3": 1,
        "g/cm3": 1000
    }
    return valor * factores_de_conversion[desde_unidad] / factores_de_conversion[hacia_unidad]

def convertir_presion(valor, desde_unidad, hacia_unidad):
    factores_de_conversion = {
        "Pa": 1,
        "bar": 1e5,
        "psi": 6894.76
    }
    return valor * factores_de_conversion[desde_unidad] / factores_de_conversion[hacia_unidad]

def convertir_temperatura(valor, desde_unidad, hacia_unidad):
    if desde_unidad == "C":
        if hacia_unidad == "F":
            return valor * 9/5 + 32
        elif hacia_unidad == "K":
            return valor + 273.15
    elif desde_unidad == "F":
        if hacia_unidad == "C":
            return (valor - 32) * 5/9
        elif hacia_unidad == "K":
            return (valor + 459.67) * 5/9
    elif desde_unidad == "K":
        if hacia_unidad == "C":
            return valor - 273.15
        elif hacia_unidad == "F":
            return valor * 9/5 - 459.67

def convertir_longitud(valor, desde_unidad, hacia_unidad):
    factores_de_conversion = {
        "m": 1,
        "ft": 0.3048,
        "in": 0.0254,
        "cm": 0.01
    }
    return valor * factores_de_conversion[desde_unidad] / factores_de_conversion[hacia_unidad]

def convertir_area(valor, desde_unidad, hacia_unidad):
    factores_de_conversion = {
        "m2": 1,
        "acres": 0.000247105,
        "ft2": 10.7639
    }
    return valor * factores_de_conversion[desde_unidad] / factores_de_conversion[hacia_unidad]


# Solicitar al usuario los datos de conversión
print("Bienvenido al convertidor de unidades")
print("Por favor, seleccione el tipo de conversión:")
print("1. Volumen")
print("2. Tasa de flujo")
print("3. Densidad")
print("4. Presión")
print("5. Temperatura")
print("6. Longitud")
print("7. Área (acres)")

opcion = int(input("Ingrese el número de la opción deseada: "))

if opcion == 1:
    desde_unidad = input("Ingrese la unidad de volumen de origen (ejemplo: m3, gal, L, ft3): ")
    hacia_unidad = input("Ingrese la unidad de volumen de destino (ejemplo: m3, gal, L, ft3): ")
    valor = float(input("Ingrese el valor a convertir: "))
    resultado = convertir_volumen(valor, desde_unidad, hacia_unidad)
    print(f"{valor} {desde_unidad} es igual a {resultado} {hacia_unidad}")
elif opcion == 2:
    desde_unidad = input("Ingrese la unidad de tasa de flujo de origen (ejemplo: m3/s, ft3/min, L/s): ")
    hacia_unidad = input("Ingrese la unidad de tasa de flujo de destino (ejemplo: m3/s, ft3/min, L/s): ")
    valor = float(input("Ingrese el valor a convertir: "))
    resultado = convertir_tasa_de_flujo(valor, desde_unidad, hacia_unidad)
    print(f"{valor} {desde_unidad} es igual a {resultado} {hacia_unidad}")
elif opcion == 3:
    desde_unidad = input("Ingrese la unidad de densidad de origen (ejemplo: kg/m3, g/cm3): ")
    hacia_unidad = input("Ingrese la unidad de densidad de destino (ejemplo: kg/m3, g/cm3): ")
    valor = float(input("Ingrese el valor a convertir: "))
    resultado = convertir_densidad(valor, desde_unidad, hacia_unidad)
    print(f"{valor} {desde_unidad} es igual a {resultado} {hacia_unidad}")
elif opcion == 4:
    desde_unidad = input("Ingrese la unidad de presión de origen (ejemplo: Pa, bar, psi): ")
    hacia_unidad = input("Ingrese la unidad de presión de destino (ejemplo: Pa, bar, psi): ")
    valor = float(input("Ingrese el valor a convertir: "))
    resultado = convertir_presion(valor, desde_unidad, hacia_unidad)
    print(f"{valor} {desde_unidad} es igual a {resultado} {hacia_unidad}")
elif opcion == 5:
    desde_unidad = input("Ingrese la unidad de temperatura de origen (ejemplo: C, F, K): ")
    hacia_unidad = input("Ingrese la unidad de temperatura de destino (ejemplo: C, F, K): ")
    valor = float(input("Ingrese el valor a convertir: "))
    resultado = convertir_temperatura(valor, desde_unidad, hacia_unidad)
    print(f"{valor} {desde_unidad} es igual a {resultado} {hacia_unidad}")
elif opcion == 6:
    desde_unidad = input("Ingrese la unidad de longitud de origen (ejemplo: m, ft, in, cm): ")
    hacia_unidad = input("Ingrese la unidad de longitud de destino (ejemplo: m, ft, in, cm): ")
    valor = float(input("Ingrese el valor a convertir: "))
    resultado = convertir_longitud(valor, desde_unidad, hacia_unidad)
    print(f"{valor} {desde_unidad} es igual a {resultado} {hacia_unidad}")
elif opcion == 7:
    desde_unidad = input("Ingrese la unidad de área de origen (ejemplo: m2, acres, ft2): ")
    hacia_unidad = input("Ingrese la unidad de área de destino (ejemplo: m2, acres, ft2): ")
    valor = float(input("Ingrese el valor a convertir: "))
    resultado = convertir_area(valor, desde_unidad, hacia_unidad)
    print(f"{valor} {desde_unidad} es igual a {resultado} {hacia_unidad}")
else:
    print("Opción no válida. Por favor, seleccione una opción del 1 al 7 para realizar una conversión.")

def main():
    # Funciones de conversión
    def convertir():
        opcion_texto = opcion_var.get()
        desde_unidad = desde_entry.get()
        hacia_unidad = hacia_entry.get()
        valor = float(valor_entry.get())

        if opcion_texto == "Volumen":
            resultado = convertir_volumen(valor, desde_unidad, hacia_unidad)
        elif opcion_texto == "Tasa de flujo":
            resultado = convertir_tasa_de_flujo(valor, desde_unidad, hacia_unidad)
        elif opcion_texto == "Densidad":
            resultado = convertir_densidad(valor, desde_unidad, hacia_unidad)
        elif opcion_texto == "Presión":
            resultado = convertir_presion(valor, desde_unidad, hacia_unidad)
        elif opcion_texto == "Temperatura":
            resultado = convertir_temperatura(valor, desde_unidad, hacia_unidad)
        elif opcion_texto == "Longitud":
            resultado = convertir_longitud(valor, desde_unidad, hacia_unidad)
        elif opcion_texto == "Área (acres)":
            resultado = convertir_area(valor, desde_unidad, hacia_unidad)
        else:
            resultado = "Opción no válida"

        resultado_label.config(text=f"{valor} {desde_unidad} es igual a {resultado} {hacia_unidad}")

    # Crear la ventana principal
    root = tk.Tk()
    root.title("Calculadora Petrolera")

    # Crear variables de control
    opciones = ["Volumen", "Tasa de flujo", "Densidad", "Presión", "Temperatura", "Longitud", "Área (acres)"]
    opcion_var = tk.StringVar()
    opcion_var.set(opciones[0])

    # Crear widgets
    titulo_label = tk.Label(root, text="Bienvenido al convertidor de unidades")
    titulo_label.grid(row=0, column=0, columnspan=2)

    tipo_label = tk.Label(root, text="Seleccione el tipo de conversión:")
    tipo_label.grid(row=1, column=0, columnspan=2)

    opcion_label = tk.Label(root, text="Opción:")
    opcion_label.grid(row=2, column=0, sticky="e")

    opcion_menu = tk.OptionMenu(root, opcion_var, *opciones)
    opcion_menu.grid(row=2, column=1, sticky="w")

    desde_label = tk.Label(root, text="Desde unidad:")
    desde_label.grid(row=3, column=0, sticky="e")

    desde_entry = tk.Entry(root)
    desde_entry.grid(row=3, column=1)

    hacia_label = tk.Label(root, text="Hacia unidad:")
    hacia_label.grid(row=4, column=0, sticky="e")

    hacia_entry = tk.Entry(root)
    hacia_entry.grid(row=4, column=1)

    valor_label = tk.Label(root, text="Valor:")
    valor_label.grid(row=5, column=0, sticky="e")

    valor_entry = tk.Entry(root)
    valor_entry.grid(row=5, column=1)

    convertir_button = tk.Button(root, text="Convertir", command=convertir)
    convertir_button.grid(row=6, column=0, columnspan=2)

    resultado_label = tk.Label(root, text="")
    resultado_label.grid(row=7, column=0, columnspan=2)

    # Ejecutar la aplicación
    root.mainloop()

if __name__ == "__main__":
    main()

