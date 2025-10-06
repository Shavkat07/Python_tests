import math
import matplotlib.pyplot as plt

# fast doubling implementation (returns tuple (F_n, F_{n+1}))
def fib_fast_doubling(n: int):
    if n == 0:
        return (0, 1)
    (a, b) = fib_fast_doubling(n >> 1)
    c = a * ((b << 1) - a)          # F_{2k} = F_k * (2*F_{k+1} - F_k)
    d = a * a + b * b               # F_{2k+1} = F_{k+1}^2 + F_k^2
    if n & 1:
        return (d, c + d)
    else:
        return (c, d)

def F(n: int) -> int:
    return fib_fast_doubling(n)[0]

# Параметры графика
N = 30  # сколько точек (можешь увеличить)
xs = list(range(N + 1))
ys = [F(n) for n in xs]

# Построение
plt.figure(figsize=(10,5))
plt.plot(xs, ys, marker='o')   # линия + точки
plt.title(f'Числа Фибоначчи F_0..F_{N}')
plt.xlabel('n (index)')
plt.ylabel('F_n')
plt.grid(True)
plt.yscale('linear')  # обычная линейная шкала; для экспоненциального роста можно логарифмировать
plt.show()
