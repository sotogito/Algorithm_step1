investment_amount = int(input())
day_of_investment = int(input())
fluctuation = map(int, input().split())

fluctuated_amount = investment_amount
for i in fluctuation:
    if i > 0:
        fluctuated_amount *= 1.0 + (i * 0.01)
    elif i < 0:
        fluctuated_amount *= 1.0 + (i * 0.01)

result = fluctuated_amount - investment_amount

print("%.0f" % result)
if result < 0:
    print("bad")
elif result == 0:
    print("same")
elif result > 0:
    print("good")
