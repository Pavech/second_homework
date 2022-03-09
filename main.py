def read_file(file: str) -> list:
    """Функция чтения файла и записи матрицы"""
    with open(file) as file_open:
        matrix = []
        for line in file_open:
            ist = line.split()
            st = list(map(int, ist))
            matrix.append(st)
        return matrix


def crater_moon(matrix: list, x: int, y: int, line: int, stl: int) -> None:
    """Функция при нахождении 1  присваивает 0, после чего начинает
    проверять соседние значения
    """
    if 0 <= x < line and 0 <= y < stl:
        if matrix[x][y] == 1:
            matrix[x][y] = 0
            crater_moon(my_input, x - 1, y, line, stl)
            crater_moon(my_input, x + 1, y, line, stl)
            crater_moon(my_input, x, y - 1, line, stl)
            crater_moon(my_input, x, y + 1, line, stl)


def calculate(my_input: list) -> int:
    """Функция подсчета кратеров"""
    count_crater = 0
    line = len(my_input)
    stl = len(my_input[0])
    for i in range(line):
        for j in range(stl):
            if my_input[i][j] == 1:
                crater_moon(my_input, i, j, line, stl)
                count_crater += 1
    return count_crater


my_input = read_file("file.txt")
print(calculate(my_input))
