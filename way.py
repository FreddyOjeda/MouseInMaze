from collections import deque
import heapq

import heapq
from collections import deque

def save_path_to_file(path, filename):
    with open(filename, "w") as file:
        for x, y in path:
            file.write(f"{x},{y}\n")

def find_path_dfs(matrix, start, end):
    def dfs(x, y):
        if x < 0 or y < 0 or x >= len(matrix[0]) or y >= len(matrix) or visited[y][x] or matrix[y][x] == 1:
            return False
        path.append((x, y))
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
    save_path_to_file(path, "path_dfs.txt")
    return path

def find_path_bfs(matrix, start, end):
    def is_valid(x, y):
        return 0 <= x < len(matrix[0]) and 0 <= y < len(matrix) and not visited[y][x] and matrix[y][x] != 1
    queue = deque([(start[0], start[1])])
    visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]
    parents = {}
    while queue:
        x, y = queue.popleft()
        visited[y][x] = True
        if (x, y) == end:
            break
        neighbors = [(x + dx, y + dy) for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]]
        valid_neighbors = [(nx, ny) for nx, ny in neighbors if is_valid(nx, ny)]
        for nx, ny in valid_neighbors:
            queue.append((nx, ny))
            parents[(nx, ny)] = (x, y)
    path = []
    current = end
    while current != start:
        path.insert(0, current)
        current = parents[current]
    path.insert(0, start)
    save_path_to_file(path, "path_bfs.txt")
    return path

def find_path_a_star(matrix, start, end):
    def heuristic(node):
        return abs(node[0] - end[0]) + abs(node[1] - end[1])
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}
    while priority_queue:
        _, current = heapq.heappop(priority_queue)
        if current == end:
            break
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_node = (current[0] + dx, current[1] + dy)
            if next_node[0] < 0 or next_node[1] < 0 or next_node[0] >= len(matrix[0]) or next_node[1] >= len(matrix):
                continue
            new_cost = cost_so_far[current] + 1
            if matrix[next_node[1]][next_node[0]] == 1 or (next_node in cost_so_far and new_cost >= cost_so_far[next_node]):
                continue
            cost_so_far[next_node] = new_cost
            priority = new_cost + heuristic(next_node)
            heapq.heappush(priority_queue, (priority, next_node))
            came_from[next_node] = current            
    path = []
    current = end
    while current != start:
        path.insert(0, current)
        current = came_from[current]
    path.insert(0, start)
    save_path_to_file(path, "path_a_star.txt")
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

# # Define la matriz y los puntos de inicio y final
# matrix = load_matrix_from_file("./matrix_output.txt")
# x_start, y_start = find_coordinates(matrix, 2)  # Buscar el punto de inicio (2)
# x_end, y_end = find_coordinates(matrix, 3) 
# start_point = (x_start, y_start)
# end_point = (x_end, y_end)
# print("Punto de inicio" , start_point)
# print("Punto de llegada: ",end_point)
# #path = find_path_dfs(matrix, start_point, end_point)
# path = find_path_bfs(matrix, start_point, end_point)
# #path = find_path_a_star(matrix, start_point, end_point)

# if path:
#     print("Camino encontrado:")
#     for x, y in path:
#         matrix[y][x] = "X"  # Marcar el camino en la matriz
#     for row in matrix:
#         print(" ".join(map(str, row)))
#     print(path)
# else:
#     print("No se encontró un camino válido.")

def solve_dfs():
    matrix = load_matrix_from_file("./matrix_output.txt")
    x_start, y_start = find_coordinates(matrix, 2)  # Buscar el punto de inicio (2)
    x_end, y_end = find_coordinates(matrix, 3) 
    start_point = (x_start, y_start)
    end_point = (x_end, y_end)
    print("Punto de inicio" , start_point)
    print("Punto de llegada: ",end_point)
    path = find_path_dfs(matrix, start_point, end_point)
    if path:
        print("Camino encontrado:")
        for x, y in path:
            matrix[y][x] = "X"  # Marcar el camino en la matriz
        for row in matrix:
            print(" ".join(map(str, row)))
        print(path)
    else:
        print("No se encontró un camino válido.")

def solve_bfs():
    matrix = load_matrix_from_file("./matrix_output.txt")
    x_start, y_start = find_coordinates(matrix, 2)  # Buscar el punto de inicio (2)
    x_end, y_end = find_coordinates(matrix, 3) 
    start_point = (x_start, y_start)
    end_point = (x_end, y_end)
    print("Punto de inicio" , start_point)
    print("Punto de llegada: ",end_point)
    path = find_path_bfs(matrix, start_point, end_point)
    if path:
        print("Camino encontrado:")
        for x, y in path:
            matrix[y][x] = "X"  # Marcar el camino en la matriz
        for row in matrix:
            print(" ".join(map(str, row)))
        print(path)
    else:
        print("No se encontró un camino válido.")

def solve_a_star():
    matrix = load_matrix_from_file("./matrix_output.txt")
    x_start, y_start = find_coordinates(matrix, 2)  # Buscar el punto de inicio (2)
    x_end, y_end = find_coordinates(matrix, 3) 
    start_point = (x_start, y_start)
    end_point = (x_end, y_end)
    print("Punto de inicio" , start_point)
    print("Punto de llegada: ",end_point)
    path = find_path_a_star(matrix, start_point, end_point)
    if path:
        print("Camino encontrado:")
        for x, y in path:
            matrix[y][x] = "X"  # Marcar el camino en la matriz
        for row in matrix:
            print(" ".join(map(str, row)))
        print(path)
    else:
        print("No se encontró un camino válido.")