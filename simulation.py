import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import time

window = tk.Tk()
window.title("Laberinto")

canvas = tk.Canvas(window, width=500, height=500)
canvas.pack()

cam = ''
cam2 = ''
cam3 = ''
cell_size = 15

def load_maze_from_file(filename):
    maze = []
    with open(filename, "r") as file:
        for line in file:
            row = [int(cell) for cell in line.strip().split()]
            maze.append(row)
    return maze

def animate_path(camN):
    camino = invert_coordinates(camN)
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

def get_simulation(algorithm):
    if algorithm == "dfs":
        cam = read_coordinates_from_file("path_dfs.txt")
        animate_path(cam)
    elif algorithm == "bfs":
        cam2 = read_coordinates_from_file("path_bfs.txt")
        animate_path(cam2)
    elif algorithm == "a_star":
        cam3 = read_coordinates_from_file("path_a_star.txt")
        animate_path(cam3)
    laberinto=load_maze_from_file("./matrix_output.txt")

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
    animate_path()
