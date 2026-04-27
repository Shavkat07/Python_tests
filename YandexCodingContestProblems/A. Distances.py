import sys


def solve():
	# Чтение x, y, z из входного потока
	try:
		x = int(sys.stdin.readline())
		y = int(sys.stdin.readline())
		z = int(sys.stdin.readline())
	except EOFError:
		return
	
	# Фиксируем c в 0
	c = 0
	# На основе z = |c - a|, полагаем a = z
	a = z
	
	# Ищем b (может быть y или -y)
	# Проверяем, подходит ли b = y для условия |a - b| = x
	if abs(a - y) == x:
		b = y
	else:
		# Если не подошло, то по условию (гарантии существования) подойдет -y
		b = -y
	
	# Вывод результата: каждое число на новой строке
	print(a)
	print(b)
	print(c)


if __name__ == "__main__":
	solve()