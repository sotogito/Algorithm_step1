f, t = map(int, input().split())


def evenOrOdd(a):
    if a % 2 == 0:
        return "짝수"
    else:
        return "홀수"


result = evenOrOdd(f + t)
f = evenOrOdd(f)
t = evenOrOdd(t)

print(f + "+" + t + "=" + result)

