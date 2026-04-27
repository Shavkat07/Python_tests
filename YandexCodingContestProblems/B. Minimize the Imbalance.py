import sys

def solve():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    a = list(map(int, data[1:n+1]))

    pairs = [abs(a[i] - a[i+1]) for i in range(n-1)]

    # prefix_max[i] = max(pairs[0..i])
    prefix_max = [0] * (n - 1)
    prefix_max[0] = pairs[0]
    for i in range(1, n - 1):
        prefix_max[i] = max(prefix_max[i-1], pairs[i])

    # suffix_max[i] = max(pairs[i..n-2])
    suffix_max = [0] * (n - 1)
    suffix_max[-1] = pairs[-1]
    for i in range(n - 3, -1, -1):
        suffix_max[i] = max(suffix_max[i+1], pairs[i])

    def get_prefix(i):   # max pairs[0..i], безопасно
        return prefix_max[i] if i >= 0 else 0

    def get_suffix(i):   # max pairs[i..n-2], безопасно
        return suffix_max[i] if i < n - 1 else 0

    best_D = prefix_max[-1]  # начальный imbalance
    best_i = 0
    best_v = a[0]

    for i in range(n):
        # Пары NOT involving i: [0..i-2] и [i+1..n-2]
        base = max(get_prefix(i - 2), get_suffix(i + 1))

        if i == 0:
            local, v = 0, a[1]
        elif i == n - 1:
            local, v = 0, a[n - 2]
        else:
            L, R = a[i-1], a[i+1]
            v = (L + R) // 2
            local = max(abs(L - v), abs(R - v))
            # Проверяем v+1 (потолочное деление)
            v2 = v + 1
            local2 = max(abs(L - v2), abs(R - v2))
            if local2 < local:
                v, local = v2, local2

        candidate = max(base, local)
        if candidate < best_D:
            best_D = candidate
            best_i = i
            best_v = v

    sys.stdout.write(f"{best_D} {best_i + 1} {best_v}\n")

solve()