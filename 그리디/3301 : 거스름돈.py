# 50000 -> 1000 -> 500 -> 10

changes = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

money = int(input())
count = 0


def calculate(count, money, change):
    count += money // change
    money -= (money // change) * change
    return count, money


for change in changes:
    count, money = calculate(count, money, change)

print(count)
