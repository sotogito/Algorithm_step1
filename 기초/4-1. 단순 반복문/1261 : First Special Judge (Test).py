a = map(int, input().split())
b = True

for i in a:
    if i % 5 == 0:
        b = False
        print(i)
        break
if b:
    print(0)

"""
10개의 수가 입력된다.

10개의 수 중 5의 배수를 하나만 출력한다.

만약 5의 배수가 없다면 0을 출력한다.
"""
