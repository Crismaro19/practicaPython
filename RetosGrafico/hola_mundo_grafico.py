import tkinter as tk
from PIL import Image, ImageTk

def saludar():
    print('Hola, mundo!')

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Mi primera ventana")
ventana.geometry("300x200")

# Crear un botón
boton = tk.Button(ventana, text="Haz clic", command=saludar)
boton.pack(pady=20)

# Abre la imagen original
imagen_original = Image.open("RetosGrafico/image.png")

# Redimensiona la imagen
imagen_redimensionada = imagen_original.resize((250, 120))

# Cargar imagen (debe ser PNG o GIF)
imagen = ImageTk.PhotoImage(imagen_redimensionada)

# Mostrarla en un Label
etiqueta = tk.Label(ventana, image=imagen)
etiqueta.pack()

# Ejecutar la ventana
ventana.mainloop()