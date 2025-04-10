import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Función para la primera pregunta 
def pregunta1():
    etiqueta_pregunta.config(text="¿A qué orden pertenece este ser vivo?")
    imagen_actual = "RetosGrafico/Trivia_Naturales/pregunta1c.png"  
    cargar_imagen(imagen_actual)

    boton1.config(text="Cnidaria", command=lambda: verificar_respuesta("correcto", pregunta2))
    boton2.config(text="Hydrozoa", command=lambda: verificar_respuesta("incorrecto", None))
    boton3.config(text="Fungi", command=lambda: verificar_respuesta("incorrecto", None))

# Función para la segunda pregunta
def pregunta2():
    etiqueta_pregunta.config(text="¿Qué tipo de planta es esta?")
    imagen_actual = "RetosGrafico/Trivia_Naturales/pregunta2l.png"  
    cargar_imagen(imagen_actual)

    boton1.config(text="Líquen", command=lambda: verificar_respuesta("incorrecto", None))
    boton2.config(text="Musgo", command=lambda: verificar_respuesta("incorrecto", None))
    boton3.config(text="Lycopodium", command=lambda: verificar_respuesta("correcto", pregunta3))

# Función para la tercera pregunta
def pregunta3():
    etiqueta_pregunta.config(text="¿Cuál es el hábitat de este animal?")
    imagen_actual = "RetosGrafico/Trivia_Naturales/pregunta3p.png"  
    cargar_imagen(imagen_actual)

    boton1.config(text="Acuático", command=lambda: verificar_respuesta("correcto", pregunta4))
    boton2.config(text="Terrestre", command=lambda: verificar_respuesta("incorrecto", None))
    boton3.config(text="Aéreo", command=lambda: verificar_respuesta("incorrecto", None))

# Función para la cuarta pregunta
def pregunta4():
    etiqueta_pregunta.config(text="¿A que filo pertenece este animal?")
    imagen_actual = "RetosGrafico/Trivia_Naturales/pregunta4a.png"
    cargar_imagen(imagen_actual) 

    boton1.config(text="Chelicerata", command=lambda: verificar_respuesta("correcto", pregunta5))
    boton2.config(text="Animal", command=lambda: verificar_respuesta("incorrecto", None))
    boton3.config(text="Scorpiones", command=lambda: verificar_respuesta("incorrecto", None))

# Función para la quinta pregunta
def pregunta5():
    etiqueta_pregunta.config(text="¿Qué fase del ciclo de vida es esta?")
    imagen_actual = "RetosGrafico/Trivia_Naturales/pregunta5p.png"  
    cargar_imagen(imagen_actual)

    boton1.config(text="Larva", command=lambda: verificar_respuesta("incorrecto", None))
    boton2.config(text="Pupa", command=lambda: verificar_respuesta("correcto", finalizar_trivia))
    boton3.config(text="Huevo", command=lambda: verificar_respuesta("incorrecto", None))

# Función para finalizar la trivia
def finalizar_trivia():
    messagebox.showinfo("Trivia Completada", "¡Felicidades, has completado la trivia de Ciencias Naturales!")
    ventana.destroy()

# fn que verifica y pasa a la siguiente pregunta
def verificar_respuesta(respuesta, siguiente_pregunta):
    if respuesta == "correcto":
        messagebox.showinfo("Respuesta Correcta", "¡Bien hecho!")
        if siguiente_pregunta:
            siguiente_pregunta()  
    else:
        messagebox.showerror("Respuesta Incorrecta", "Inténtalo de nuevo")

# Función para cargar la imagen correspondiente a cada pregunta y redimensionamiento 
def cargar_imagen(ruta):
    try:
        imagen_original = Image.open(ruta)
        imagen_redimensionada = imagen_original.resize((250, 250))
        imagen = ImageTk.PhotoImage(imagen_redimensionada)
        label_imagen.config(image=imagen)
        label_imagen.image = imagen  
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo cargar la imagen: {e}")

# Ventana principal
ventana = tk.Tk()
ventana.title("Trivia de Ciencias Naturales")
ventana.geometry("730x400")
ventana.config(bg="#DDF4FF")  # Fondo azul claro

# Marco para la imagen
marco = tk.Frame(ventana, bg="#DDF4FF")
marco.pack(side="left", padx=20, pady=20)

# Marco para la imagen con borde
marco_imagen = tk.Frame(marco, bg="#FFB6C1", padx=5, pady=5)  # Marco rosado
marco_imagen.pack(pady=10)

label_imagen = tk.Label(marco_imagen)
label_imagen.pack()

# Marco para preguntas y respuestas
marco_preguntas = tk.Frame(ventana, bg="#DDF4FF")
marco_preguntas.pack(side="right", padx=20, pady=20)

etiqueta_pregunta = tk.Label(marco_preguntas, text="", font=("Comic Sans MS", 16), bg="#DDF4FF", fg="#333333")
etiqueta_pregunta.pack(pady=10)

# 3 opciones de respuesta como marcaba uno de los requerimientos establecidos en la guia 
boton1 = tk.Button(marco_preguntas, font=("Arial", 12), bg="#A3D5D3", fg="#000000", relief="groove", bd=2, width=15, height=1)
boton1.pack(pady=5)

boton2 = tk.Button(marco_preguntas, font=("Arial", 12), bg="#A3D5D3", fg="#000000", relief="groove", bd=2, width=15, height=1)
boton2.pack(pady=5)

boton3 = tk.Button(marco_preguntas, font=("Arial", 12), bg="#A3D5D3", fg="#000000", relief="groove", bd=2, width=15, height=1)
boton3.pack(pady=5)

# Iniciar la trivia con la primera pregunta
# pregunta1()

# Ejecutar la ventana
ventana.mainloop()
