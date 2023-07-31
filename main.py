import json
from tkinter import *

# Cargar la base de datos JSON
with open('C:/Users/Nahue/OneDrive/Escritorio/PROGRAMACION/PYTHON/Cilan/test/db.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

windows = Tk()
windows.title("Consultor de Prefijos")

# Label
text_1 = Label(windows, text="Inserte el número de teléfono...")
text_1.grid(row=0, column=0, columnspan=50, padx=50, pady=5)

# Input
input = Entry(windows, width=70)
input.grid(row=1, column=0, columnspan=50, padx=50, pady=5)

def consultar_precio():
    numero_telefonico = input.get()
    prefijo = numero_telefonico[:3]

    # Consultar el precio en la "base de datos"
    if prefijo in data['prefijos']:
        precio = data['prefijos'][prefijo]['precio']
        pais = data['prefijos'][prefijo]['pais']
        ciudad = data['prefijos'][prefijo]['ciudad']
        result.config(text=f'El prefijo: {prefijo}, es de {ciudad}, {pais}con un costo de ${precio} por minuto')
        # result.config(text={prefijo})
    else:
        result.config(text='El prefijo no está registrado en la base de datos')

# Boton
btn_Set = Button(windows, text='Consultar', width=15, height=1, command=consultar_precio)
btn_Set.grid(row=3, columnspan=50, padx=2, pady=2)

# Label resultado
result = Label(windows, text="", fg='red')
result.grid(row=2, columnspan=50)

windows.mainloop()
