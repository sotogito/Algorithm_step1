a = int(input())

for i in range(1, 10):  # 1~9
    # print(a + "*" + i + "=" + a * i)
    # 숫자와 문자열을+ 연산자로 잇지 못함
    print(str(a) + "*" + str(i) + "=" + str(a * i))
