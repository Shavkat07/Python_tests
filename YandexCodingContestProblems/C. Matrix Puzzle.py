import sys
import numpy as np

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n, m = int(data[idx]), int(data[idx+1])
    idx += 2
    a = np.array(data[idx:idx+n*m], dtype=np.int64).reshape(n, m)

    # Горизонтальная циклическая сумма: a[i,j] * a[i,(j+1)%m]
    H_circ = int(np.sum(a * np.roll(a, -1, axis=1)))

    # f[c] = сумма по строкам: a[i,(c-1)%m] * a[i,c]
    f = np.sum(np.roll(a, 1, axis=1) * a, axis=0)
    min_f = int(np.min(f))

    # Вертикальная циклическая сумма: a[i,j] * a[(i+1)%n,j]
    V_circ = int(np.sum(a * np.roll(a, -1, axis=0)))

    # g[r] = сумма по столбцам: a[(r-1)%n,j] * a[r,j]
    g = np.sum(np.roll(a, 1, axis=0) * a, axis=1)
    min_g = int(np.min(g))

    print(H_circ - min_f + V_circ - min_g)

solve()