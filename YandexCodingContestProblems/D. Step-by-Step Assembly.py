import sys


def solve():
	data = sys.stdin.read().split()
	n = int(data[0])
	t1, t2, t3 = int(data[1]), int(data[2]), int(data[3])
	
	f2 = 0
	f3 = 0
	for j in range(1, n + 1):
		f2 = max((2 * j - 1) * t1, f2) + t2
		f3 = max(2 * j * t1, f2, f3) + t3
	
	print(f3)


solve()