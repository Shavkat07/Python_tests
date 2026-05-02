a = [1, 2, 3, 4, 5, 42, 5, 5, 24, 22, 5, 52]
b = [3, 2, 4, 53, 2, 56, 44, 3, 65, 34, 63, 36]

def var(x: list):
	n = len(x)
	E_X = sum(x) / n
	answer = sum([(x[i] - E_X) ** 2 for i in range(n)])

	return answer / (n - 1)


print(var(a))


def cov(x: list[int], y: list[int]) -> float:
	n = len(x)
	mean_x = sum(x) / n
	mean_y = sum(y) / n
	answer = sum([((x[i] - mean_x) * (y[i] - mean_y)) for i in range(n)])
	
	return answer  / (n - 1)

print(cov(a, b))