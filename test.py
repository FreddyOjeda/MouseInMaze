import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from ArrayMaker import arrayMaker
from way import solve_dfs, solve_bfs, solve_a_star
import time

window = tk.Tk()
window.title("Proyecto de inteligencia artificial generativa - IAG")

# Crear los frames para las columnas
frame_col1 = tk.Frame(window)
frame_col2 = tk.Frame(window)
frame_col3 = tk.Frame(window)
frame_col4 = tk.Frame(window)

frame_col1.grid(column=0, row=0, padx=10, pady=10)
frame_col2.grid(column=1, row=0, padx=10, pady=10)
frame_col3.grid(column=2, row=0, padx=10, pady=10)
frame_col4.grid(column=3, row=0, padx=10, pady=10)

text_style = {"font": ("Helvetica", 12), "fg": "black"}
button_style = {"font": ("Helvetica", 10), "bg": "green", "fg": "white"}

laberinto_image = None

def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.gif")])
    if file_path:
        show_simulation_images(file_path)

def solve_mazes():
    solve_dfs()
    solve_bfs()
    solve_a_star()

# Agregar contenido a la columna 1
label_left_top = tk.Label(frame_col1, text="Por favor seleccione el \n laberinto a solucionar:", **text_style)
button_select_image = tk.Button(frame_col1, text="Seleccionar Imagen", command=select_image)
button_solve_mazes = tk.Button(frame_col1, text="Resolver Laberintos", command=solve_mazes, **button_style)
label_members = tk.Label(frame_col1, text="Integrandes del grupo:\n\n- Mayerly Andrea Salcedo\n- Diego Alejandro Corredor Rojas\n- Freddy Esteban Ojeda Cogua", **text_style)

label_left_top.pack()
button_select_image.pack()
button_solve_mazes.pack()
label_members.pack()

# Crear los canvas para mostrar las imágenes en las columnas 2, 3 y 4
canvas_col2 = tk.Canvas(frame_col2, width=500, height=800)  # Ajusta el ancho y alto según tus necesidades
canvas_col3 = tk.Canvas(frame_col3, width=500, height=800)  # Ajusta el ancho y alto según tus necesidades
canvas_col4 = tk.Canvas(frame_col4, width=500, height=800)  # Ajusta el ancho y alto según tus necesidades

canvas_col2.pack()
canvas_col3.pack()
canvas_col4.pack()

def load_image(filename):
    image = Image.open(filename)
    return image

def animate_path(way, canvas):
    for step in way:
        row, col = step
        x1 = col * cell_size + cell_size // 4
        y1 = row * cell_size + cell_size // 4
        x2 = x1 + cell_size // 2
        y2 = y1 + cell_size // 2
        canvas.create_oval(x1, y1, x2, y2, fill="green")
        window.update()
        time.sleep(0.05)
        canvas.update()

def invert_coordinates(coordinates):
    inverted_coordinates = [(col, row) for row, col in coordinates]
    return inverted_coordinates

def read_coordinates_from_file(filename):
    coordinates = []
    with open(filename, "r") as file:
        for line in file:
            x, y = map(int, line.strip().split(","))
            coordinates.append((x, y))
    return coordinates

def load_maze_from_file(filename):
    maze = []
    with open(filename, "r") as file:
        for line in file:
            row = [int(cell) for cell in line.strip().split()]
            maze.append(row)
    return maze

laberinto = load_maze_from_file("./matrix_output.txt")
cam1 = read_coordinates_from_file("path_dfs.txt")
cam2 = read_coordinates_from_file("path_bfs.txt")
cam3 = read_coordinates_from_file("path_a_star.txt")

maze_width = len(laberinto[0])  # Ancho del laberinto
maze_height = len(laberinto)     # Alto del laberinto

camino1 = invert_coordinates(cam1)
camino2 = invert_coordinates(cam2)
camino3 = invert_coordinates(cam3)
cell_size = 15

def get_simulation_images(laberinto, caminito, canvas):
    canvas.delete("all")  # Limpiar el canvas antes de dibujar
    for i in range(len(laberinto)):
        for j in range(len(laberinto[i])):
            x1 = j * cell_size
            y1 = i * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size
            
            if laberinto[i][j] == 1:
                canvas.create_rectangle(x1, y1, x2, y2, fill="black")
            else:
                canvas.create_rectangle(x1, y1, x2, y2, fill="white")
    animate_path(caminito, canvas)

# Dentro de la función show_simulation_images
def show_simulation_images(path_image):
    laberinto_image32 = arrayMaker(path_image)

    # Llamar a get_simulation_images con los caminos y canvas
    cam1 = read_coordinates_from_file("path_dfs.txt")
    get_simulation_images(laberinto, cam1, canvas_col2)

    cam2 = read_coordinates_from_file("path_bfs.txt")
    get_simulation_images(laberinto, cam2, canvas_col3)

    cam3 = read_coordinates_from_file("path_a_star.txt")
    get_simulation_images(laberinto, cam3, canvas_col4)

    # Configurar las imágenes en los cuadros correspondientes
    label_col2 = tk.Label(frame_col2, image=laberinto_image32, text="Algortimo a")
    label_col3 = tk.Label(frame_col3, image=laberinto_image32, text="Algortimo b")
    label_col4 = tk.Label(frame_col4, image=laberinto_image32, text="Algortimo c")

    label_col2.image = laberinto_image32
    label_col3.image = laberinto_image32
    label_col4.image = laberinto_image32

    label_col2.pack()
    label_col3.pack()
    label_col4.pack()

# Iniciar el bucle principal de la interfaz gráfica
window.mainloop()
