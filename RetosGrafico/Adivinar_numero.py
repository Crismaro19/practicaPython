import tkinter as tk
from tkinter import ttk

def iniciar_carga():
    barra.start()  # Empieza a moverse
    ventana.after(5000, finalizar_carga)  # Simula que se detiene luego de 3 segundos


def finalizar_carga():
    barra.stop()
    barra.pack_forget()  # Ocultar la barra
    texto = entrada.get()
    etiqueta_resultado.config(text=f"El numero que pensaste es: {texto}")



# Crear ventana principal
ventana = tk.Tk()

style = ttk.Style()
style.theme_use('clam')

ventana.title("Adivinar numero")
ventana.geometry("300x200")

# Etiqueta
etiqueta = tk.Label(ventana, text="Escribe el numero que piensas:")
etiqueta.pack(pady=5)

# Campo de entrada
entrada = tk.Entry(ventana)
entrada.pack(pady=5)

# Botón
boton = tk.Button(ventana, text="Adivinar", command=iniciar_carga)
boton.pack(pady=5)

barra = ttk.Progressbar(ventana, mode='indeterminate')
barra.pack(pady=20, fill='x', padx=20)


# Resultado
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack(pady=5)

# Ejecutar la ventana
ventana.mainloop()