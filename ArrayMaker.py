from PIL import Image

def load_image_and_convert_to_matrix(image_path):
    img = Image.open(image_path)
    img = img.convert("L")  # Convertir a escala de grises
    img = img.point(lambda p: p < 128 and 1)  # Convertir a 1s (paredes) y 0s (espacios libres)

    width, height = img.size
    matrix = []
    for y in range(height):
        row = []
        for x in range(width):
            pixel = img.getpixel((x, y))
            row.append(pixel)
        matrix.append(row)

    return matrix

def is_redish(pixel):
    # Verifica si el pixel tiene tonalidades de rojo
    r, g, b = pixel
    return r > 150 and g < 100 and b < 100


def is_yellowish(pixel):
    # Verifica si el pixel tiene tonalidades de amarillo
    r, g, b = pixel
    return r > 150 and g > 150 and b < 100

def is_light_gray(pixel):
    # Verifica si el pixel tiene tonalidades de blanco (gris claro)
    r, g, b = pixel
    return r > 200 and g > 200 and b > 200

def is_dark_gray(pixel):
    # Verifica si el pixel tiene tonalidades de negro (gris oscuro)
    r, g, b = pixel
    return r < 50 and g < 50 and b < 50

def load_image_and_convert_to_matrix2(image_path):
    img = Image.open(image_path)
    img = img.convert("RGB")  # Convertir a formato RGB

    width, height = img.size
    matrix = []
    for y in range(height):
        row = []
        for x in range(width):
            pixel = img.getpixel((x, y))
            if is_light_gray(pixel):  # Tonos de blanco (gris claro)
                row.append(0)
            elif is_dark_gray(pixel):  # Tonos de negro (gris oscuro)
                row.append(1)
            elif is_redish(pixel):  # Tonos de rojo
                row.append(2)
            elif is_yellowish(pixel):  # Tonos de amarillo
                row.append(3)
            else:
                row.append(-1)  # Valor negativo para otros colores no especificados
        matrix.append(row)

    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

def export_matrix_to_txt(matrix, output_file):
    with open(output_file, "w") as f:
        for row in matrix:
            f.write(" ".join(map(str, row)) + "\n")

if __name__ == "__main__":
    #image_path = "./images/pixil.png"
    image_path = "./images/frameL.png"
    matrix = load_image_and_convert_to_matrix2(image_path)
    output_file = "matrix_output.txt"  # Cambia el nombre del archivo si lo deseas
    export_matrix_to_txt(matrix, output_file)


