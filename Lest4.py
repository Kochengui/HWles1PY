def transpose_matrix(matrix):
    # Получаем количество строк и столбцов в матрице
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Создаем новую матрицу для транспонирования
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]
    
    # Транспонируем матрицу
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    
    return transposed

# Пример использования функции
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

transposed_matrix = transpose_matrix(matrix)

# Выводим исходную и транспонированную матрицы
print("Исходная матрица:")
for row in matrix:
    print(row)
    


def create_dict(**kwargs):
    result = {}
    for key, value in kwargs.items():
        key_str = str(key) if not isinstance(key, (int, float, complex)) else key
        result[value] = key_str
    return result

# Пример использования функции
result_dict = create_dict(a=10, b='hello', c=3.14)
print(result_dict)
