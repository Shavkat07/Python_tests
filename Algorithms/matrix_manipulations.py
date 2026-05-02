matrix = [[4, 2, 3, 1],
          [6, -3, 0, 2],
          [2, -1, 3, -4],
          [0, 2, 4, 1]]

mat2 = [[3, 2, 1],
        [2, 5, 3],
        [3, 4, 3]]

mat3 = [[1, 1, 1, 1],
        [1, 1, -1, -1],
        [1, -1, 0, 0],
        [1, 0, 1, -1]]

def transpose(mtrx):
	rows = len(mtrx)
	cols = len(mtrx[0])
	res = [[0 for _ in range(rows)] for _ in range(cols)]
	
	for i in range(rows):
		for j in range(cols):
			res[j][i] = mtrx[i][j]
	return res
	

def minor(mx, i, j):
	mnr = [
		[row[col_id] for col_id in range(len(row)) if col_id != j]
		for row_id, row in enumerate(mx) if row_id != i
	]
	return mnr


def determinant(mtrx):
	n = len(mtrx)
	if n == 1:
		return mtrx[0][0]
	
	if n == 2:
		return mtrx[0][0] * mtrx[1][1] - mtrx[0][1] * mtrx[1][0]
	
	det = 0
	i = 0
	for j in range(n):
		a = mtrx[i][j]
		det += a * ((-1) ** (i + j)) * determinant(minor(mtrx, i, j))
	
	return det


def inverse(mtrx):
	det = determinant(mtrx)
	
	if det == 0:
		return None
	
	A = []
	
	transposed_mtrx = transpose(mtrx)
	for i in range(len(mtrx)):
		A.append([])
		for j in range(len(mtrx[i])):
			A[i].append(((-1) ** (i + j)) * determinant(minor(transposed_mtrx, i, j)))
			
	
	return [[elem / det for elem in row] for row in A]
	
	
print(inverse(mat3))

# print(transpose(mat2))