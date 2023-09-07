import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import time

window = tk.Tk()
window.title("Laberinto")

canvas = tk.Canvas(window, width=500, height=500)
canvas.pack()

def load_image(filename):
    image = Image.open(filename)
    return image

def invert_coordinates(coordinates):
    inverted_coordinates = [(col, row) for row, col in coordinates]
    return inverted_coordinates

def animate_path():
    for step in camino:
        row, col = step
        x1 = col * cell_size + cell_size // 4
        y1 = row * cell_size + cell_size // 4
        x2 = x1 + cell_size // 2
        y2 = y1 + cell_size // 2
        canvas.create_oval(x1, y1, x2, y2, fill="green")
        window.update()
        time.sleep(0.05)
        canvas.update()

def run_algorithms():
    global camino
    camino = invert_coordinates(cam2)
    animate_path()

def read_coordinates_from_file(filename):
    coordinates = []
    with open(filename, "r") as file:
        for line in file:
            x, y = map(int, line.strip().split(","))
            coordinates.append((x, y))
    return coordinates

laberinto_image = None
camino1 = []
camino2 = []
camino3 = []
cam = read_coordinates_from_file("path_dfs.txt")
cam2 = read_coordinates_from_file("path_bfs.txt")
cam3 = read_coordinates_from_file("path_a_star.txt")
print("cam:", cam)
print("cam2:", cam2)
print("cam3:", cam3)
cell_size = 15

def select_image():
    global laberinto_image
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.gif")])
    if file_path:
        laberinto_image = load_image(file_path)
        draw_labyrinth()

def draw_labyrinth():
    if laberinto_image:
        img = ImageTk.PhotoImage(laberinto_image)
        canvas.create_image(0, 0, anchor=tk.NW, image=img)
        canvas.image = img

select_button = tk.Button(window, text="Seleccionar Imagen", command=select_image)
select_button.pack()

run_button = tk.Button(window, text="Ejecutar Algoritmos", command=run_algorithms)
run_button.pack()

window.mainloop()
