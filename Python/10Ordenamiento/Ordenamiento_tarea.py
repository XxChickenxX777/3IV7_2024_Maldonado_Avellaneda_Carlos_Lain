import tkinter as tk
from tkinter import messagebox
import time


# Funciones de ordenamiento
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# Variables globales
original_numbers = []


# Función principal
def sort_numbers():
    global original_numbers
    try:
        # Si es la primera vez, leer la entrada
        if not original_numbers:
            numbers = list(map(int, entry.get().split(',')))
            if len(numbers) > 40:
                messagebox.showerror("Error", "La lista no puede tener más de 40 números.")
                return
            original_numbers = numbers

        sort_method = method_var.get()

        if sort_method == "Bubble Sort":
            start_time = time.time()
            sorted_numbers = bubble_sort(original_numbers[:])
        elif sort_method == "Selection Sort":
            start_time = time.time()
            sorted_numbers = selection_sort(original_numbers[:])
        elif sort_method == "Insertion Sort":
            start_time = time.time()
            sorted_numbers = insertion_sort(original_numbers[:])
        elif sort_method == "Merge Sort":
            start_time = time.time()
            sorted_numbers = merge_sort(original_numbers[:])
        elif sort_method == "Quick Sort":
            start_time = time.time()
            sorted_numbers = quick_sort(original_numbers[:])
        else:
            messagebox.showerror("Error", "Por favor, selecciona un método de ordenamiento.")
            return

        end_time = time.time()
        elapsed_time = end_time - start_time

        result_label.config(
            text=f"Original: {original_numbers}\n"
                 f"Ordenada: {sorted_numbers}\n"
                 f"Tiempo: {elapsed_time:.6f} segundos"
        )
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa una lista válida de números separados por comas.")


def reset():
    """Reinicia el proceso, permitiendo probar otro método de ordenamiento."""
    global original_numbers
    if not original_numbers:
        messagebox.showerror("Error", "Primero ingresa y ordena una lista.")
        return

    method_var.set("Bubble Sort")
    result_label.config(text="")

root = tk.Tk()
root.title("Ordenamiento de Números")

tk.Label(root, text="Ingresa una lista de números separados por comas (máx. 40):").pack(pady=5)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

tk.Label(root, text="Selecciona un método de ordenamiento:").pack(pady=5)

method_var = tk.StringVar(value="Bubble Sort")
methods = ["Bubble Sort", "Selection Sort", "Insertion Sort", "Merge Sort", "Quick Sort"]
for method in methods:
    tk.Radiobutton(root, text=method, variable=method_var, value=method).pack(anchor="w")

tk.Button(root, text="Ordenar", command=sort_numbers).pack(pady=10)
tk.Button(root, text="Reiniciar", command=reset).pack(pady=5)

result_label = tk.Label(root, text="", justify="left", wraplength=400)
result_label.pack(pady=10)

root.mainloop()
