
def find_path(matrix, start, end):
    def dfs(x, y):
        if x < 0 or y < 0 or x >= len(matrix[0]) or y >= len(matrix) or visited[y][x] or matrix[y][x] == 1:
            return False
        
        path.append((x, y))
        print(path)
        visited[y][x] = True

        if (x, y) == end:
            return True
        
        if dfs(x + 1, y) or dfs(x - 1, y) or dfs(x, y + 1) or dfs(x, y - 1):
            return True
        
        path.pop()
        return False

    path = []
    visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]
    dfs(start[0], start[1])
    return path

def load_matrix_from_file(file_path):
    matrix = []
    with open(file_path, "r") as f:
        for line in f:
            row = [int(cell) for cell in line.strip().split()]
            matrix.append(row)
    return matrix

def find_coordinates(matrix, value):
    for y, row in enumerate(matrix):
        for x, cell in enumerate(row):
            if cell == value:
                return x, y
    return None, None


# Define la matriz y los puntos de inicio y final
matrix = load_matrix_from_file("./matrix_output3.txt")

x_start, y_start = find_coordinates(matrix, 2)  # Buscar el punto de inicio (2)
x_end, y_end = find_coordinates(matrix, 3) 
start_point = (x_start, y_start)
end_point = (x_end, y_end)
#start_point=(56, 26)
#end_point=(6,61)
print("Punto de inicio" , start_point)
print("Punto de llegada: ",end_point)
path = find_path(matrix, start_point, end_point)

if path:
    print("Camino encontrado:")
    for x, y in path:
        matrix[y][x] = "X"  # Marcar el camino en la matriz
    for row in matrix:
        print(" ".join(map(str, row)))
else:
    print("No se encontró un camino válido.")