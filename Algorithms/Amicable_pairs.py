n = 1000000
divisor_sum = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(i, n + 1, i):
        divisor_sum[j] += i

amicable_pairs = []
for i in range(1, n + 1):
    j = divisor_sum[i]
    if j != i and j <= n and divisor_sum[j] == i:
        if i < j:  # To avoid duplicate pairs
            amicable_pairs.append((i, j))

print("Friendly number pairs (amiable numbers) found:")
for a, b in amicable_pairs:
    print(f"({a}, {b})")
