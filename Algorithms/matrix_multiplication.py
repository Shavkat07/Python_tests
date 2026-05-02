import time
from typing import List

A = [[3, -3, -3], [-3, -2, -5], [5, -1, -4], [-4, 3, -3]]
B = [[-4, 1, 5, -3, 0], [1, -4, 2, 1, -5], [-5, -5, 5, -5, -4]]

matrix_1a = [
    [3, -1],
    [-1, 2]
]
matrix_1b = [
    [1, 1],
    [3, 1]
]

# 2) Произведение двух матриц 3x3
matrix_2a = [
    [1, 1, 3],
    [0, 2, 1],
    [-1, 0, 4]
]
matrix_2b = [
    [3, -1, 0],
    [0, 1, 1],
    [2, 0, 1]
]

# 3) Произведение матрицы 4x3 на матрицу 3x2
matrix_3a = [
    [0, -1, 2],
    [2, 1, 1],
    [3, 0, 1],
    [3, 7, 1]
]
matrix_3b = [
    [3, 1],
    [2, 1],
    [1, 0]
]

# 4) Произведение матрицы 3x3 на вектор-столбец 3x1
matrix_4a = [
    [3, 2, 1],
    [-2, 0, 3],
    [3, -1, 2]
]
matrix_4b = [
    [2],
    [4],
    [3]
]

start = time.time()
def matrix_multiplication(a: List[List], b: List[List]) -> List:
	cols = len(a[0])  # ---> 3
	rows = len(b)  # ---> 3
	result = [[]]
	h = 0
	l = 0
	if rows == cols:
		while len(result) <= len(a):
			C_i = []
			for j in range(cols):
				yigindi = a[l][j] * b[j][h]
				C_i.append(yigindi)
			
			result[l].append(sum(C_i))
			h += 1
			if len(result[l]) == len(b[0]):
				l += 1
				h = 0
				result.append([])
		return [p for p in result if p]
	else:
		return []
elapsed = time.time() - start

for i in matrix_multiplication(matrix_4a, matrix_4b):
	print(i)
print(elapsed)