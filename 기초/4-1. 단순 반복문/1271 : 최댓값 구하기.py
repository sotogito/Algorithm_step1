i = int(input())
a = map(int, input().split())

# maxNum = max(a)
maxNum = 0

for num in a:
    if num > maxNum:
        maxNum = num

print(maxNum)
