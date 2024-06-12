a, b = map(int, input().split())

c = []

for i in range(1, max(a, b) + 1):
    odd = 0
    even = 0

    odd += i
    c.append(odd)

    even += i * 10
    c.append(even)

print(c[a - 1] + c[b - 1])
