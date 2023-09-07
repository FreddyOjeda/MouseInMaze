import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from ArrayMaker import arrayMaker
from way import solve_dfs, solve_bfs, solve_a_star

window = tk.Tk()
window.title("Proyecto de inteligencia artificial generativa - IAG")
canvas = tk.Canvas(window, width=1300, height=300)
canvas.pack()

frame_horizontal = tk.Frame(window)

subframe_left_top = tk.Frame(frame_horizontal)
subframe_right_top = tk.Frame(frame_horizontal)
subframe_left_bottom = tk.Frame(frame_horizontal)
subframe_right_bottom = tk.Frame(frame_horizontal)
subframe_left_top.pack(side=tk.LEFT, padx=10, pady=10)
subframe_right_top.pack(side=tk.RIGHT, padx=10, pady=10)
subframe_left_bottom.pack(side=tk.LEFT, padx=10, pady=10)
subframe_right_bottom.pack(side=tk.RIGHT, padx=10, pady=10)

text_style = {"font": ("Helvetica", 12), "fg": "black"}
button_style = {"font": ("Helvetica", 10), "bg": "green", "fg": "white"}

laberinto_image = None




def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.gif")])
    if file_path:
        show_images_in_frames(file_path)

def load_image(filename):
    image = Image.open(filename)
    return image

def show_images_in_frames(path_image):
    laberinto_image32 = arrayMaker(path_image)

    label_right_top.configure(image=laberinto_image32, text="Algortimo a")
    label_right_top.image = laberinto_image32

    label_left_bottom.configure(image=laberinto_image32, text="Algortimo b")
    label_left_bottom.image = laberinto_image32

    label_right_bottom.configure(image=laberinto_image32, text="Algortimo c")
    label_right_bottom.image = laberinto_image32


#Ejecutar algoritmos
def solve_algorithms():
    solve_dfs()
    solve_bfs()
    solve_a_star()

# Agregar contenido a las subsecciones (puedes agregar widgets aquí)
label_left_top = tk.Label(subframe_left_top, text="Por favor seleccione el \n laberinto a solucionar:", **text_style)
button_select_image = tk.Button(subframe_left_top, text="Seleccionar Imagen", command=select_image)
button_run_algorithms = tk.Button(subframe_left_top, text="Ejecutar Algoritmos", command=solve_algorithms, **button_style)
label_members = tk.Label(subframe_left_top, text="Integrandes del grupo:\n\n- Mayerly Andrea Salcedo\n- Diego Alejandro Corredor Rojas\n- Freddy Esteban Ojeda Cogua", **text_style)
label_right_top = tk.Label(subframe_right_top, text="Algortimo a")
label_left_bottom = tk.Label(subframe_left_bottom, text="Algortimo b")
label_right_bottom = tk.Label(subframe_right_bottom, text="Algortimo c")

# Acomodar los widgets en la subsección izquierda superior
label_left_top.pack()
button_select_image.pack()
button_run_algorithms.pack()
label_members.pack()
label_right_top.pack()
label_left_bottom.pack()
label_right_bottom.pack()

# Acomodar las subsecciones en la sección horizontal
subframe_left_top.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
subframe_right_top.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
subframe_left_bottom.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
subframe_right_bottom.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Acomodar la sección horizontal en la ventana
frame_horizontal.pack(fill=tk.BOTH, expand=True)

# Iniciar el bucle principal de la interfaz gráfica
window.mainloop()
