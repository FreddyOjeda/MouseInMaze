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

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

def export_matrix_to_txt(matrix, output_file):
    with open(output_file, "w") as f:
        for row in matrix:
            f.write(" ".join(map(str, row)) + "\n")

if __name__ == "__main__":
    image_path = "./images/l3.jpg"
    matrix = load_image_and_convert_to_matrix(image_path)
    output_file = "matrix_output.txt"  # Cambia el nombre del archivo si lo deseas
    export_matrix_to_txt(matrix, output_file)
