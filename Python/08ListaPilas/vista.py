# vista.py

import tkinter as tk
from tkinter import messagebox

def crear_interfaz(logica_pila):
    # Crear la ventana
    ventana = tk.Tk()
    ventana.title("Manejo de Pila")
    ventana.geometry("400x400")

    # Crear la pila
    pila = logica_pila["crear_pila"]()

    # Funciones de la interfaz
    def manejar_apilar():
        elemento = entrada_elemento.get()
        if elemento:
            logica_pila["apilar"](pila, elemento)
            actualizar_pila()
            entrada_elemento.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada vacía", "Por favor, ingresa un elemento")

    def manejar_desapilar():
        try:
            elemento = logica_pila["desapilar"](pila)
            messagebox.showinfo("Desapilar", f"Elemento desapilado: {elemento}")
            actualizar_pila()
        except IndexError as e:
            messagebox.showerror("Error", str(e))

    def manejar_cima():
        try:
            elemento = logica_pila["cima"](pila)
            messagebox.showinfo("Cima", f"Elemento en la cima: {elemento}")
        except IndexError as e:
            messagebox.showerror("Error", str(e))

    def manejar_tamano():
        tam = logica_pila["tamano"](pila)
        messagebox.showinfo("Tamaño", f"El tamaño de la pila es: {tam}")

    def manejar_mostrar():
        try:
            pila_actual = logica_pila["mostrar_pila"](pila)
            messagebox.showinfo("Pila Actual", pila_actual)
        except IndexError as e:
            messagebox.showerror("Error", str(e))

    def actualizar_pila():
        pila_actual = logica_pila["mostrar_pila"](pila)
        etiqueta_pila.config(text=pila_actual)

    # Componentes de la interfaz
    tk.Label(ventana, text="Manejo de una Pila", font=("Arial", 16)).pack(pady=10)

    entrada_elemento = tk.Entry(ventana, width=30)
    entrada_elemento.pack(pady=5)

    tk.Button(ventana, text="Apilar", command=manejar_apilar).pack(pady=5)
    tk.Button(ventana, text="Desapilar", command=manejar_desapilar).pack(pady=5)
    tk.Button(ventana, text="Ver Cima", command=manejar_cima).pack(pady=5)
    tk.Button(ventana, text="Ver Tamaño", command=manejar_tamano).pack(pady=5)
    tk.Button(ventana, text="Mostrar Pila", command=manejar_mostrar).pack(pady=5)

    etiqueta_pila = tk.Label(ventana, text="Pila Actual: []", font=("Arial", 12))
    etiqueta_pila.pack(pady=20)

    ventana.mainloop()
