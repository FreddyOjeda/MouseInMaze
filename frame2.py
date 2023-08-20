import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import colorsys

def open_image():
    global hsl_colors  # Declarar hsl_colors como variable global
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp")])
    if file_path:
        image = Image.open(file_path)
        image.thumbnail((400, 400))  # Redimensionar la imagen para que quepa en la ventana
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo  # ¡Importante! Mantener una referencia para evitar que el recolector de basura lo elimine
        
        # Obtener los colores únicos de la imagen
        unique_colors = set(image.getdata())
        
        # Convertir los colores RGB a valores HSL y almacenarlos en hsl_colors
        hsl_colors = []
        for color in unique_colors:
            r, g, b = color
            h, l, s = colorsys.rgb_to_hls(r / 255, g / 255, b / 255)
            hsl_colors.append((h, s, l))
        
        # Imprimir la matriz de '1' y '0' para colores oscuros y claros
        print_matrix(hsl_colors)

def is_dark_color(h, s, l, threshold=0.5):
    return l < threshold

def print_matrix(hsl_colors):
    dark_threshold = 0.5
    dark_matrix = []
    
    for h, s, l in hsl_colors:
        dark_value = 1 if is_dark_color(h, s, l, dark_threshold) else 0
        dark_matrix.append(dark_value)
    
    # Convertir la matriz en una cadena para imprimir
    matrix_size = int(len(dark_matrix) ** 0.5)
    matrix = []
    
    # Dividir la cadena en segmentos de longitud igual al tamaño de la matriz
    for i in range(0, len(dark_matrix), matrix_size):
        matrix.append(dark_matrix[i:i+matrix_size])
    
    # Imprimir la matriz organizada
    for row in matrix:
        print(row)

# Crear la ventana principal
root = tk.Tk()
root.title("Proyecto Final IA Generativa")

# Botón para abrir una imagen
open_button = tk.Button(root, text="Abrir Imagen", command=open_image)
open_button.pack(pady=10)

# Etiqueta para mostrar la imagen
image_label = tk.Label(root)
image_label.pack()

# Iniciar el bucle de eventos
root.mainloop()
