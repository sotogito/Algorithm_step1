"""
파파 파스타 가게는 점심 추천 파스타와 생과일 쥬스 세트 메뉴가 인기가 좋다.

이 세트 메뉴를 주문하면 그 날의 3 종류의 파스타와 2 종류의 생과일 쥬스에서 하나씩 선택한다.

파스타와 생과일 쥬스의 가격 합계에서 10%를 더한 금액이 대금된다.

어느 날의 파스타와 생과일 쥬스의 가격이 주어 졌을 때, 그 날 세트 메뉴의 대금의 최소값을 구하는 프로그램을 작성하라.

(모든 파스타와 생과일 쥬스의 가격은 100 원이상 2000원 이하이다.)
"""
"""
1. 파스타의 최소값을 구한다
2. 주스의 최소값을 고른다/
3. 계산한다.
"""

pasta1 = int(input()) #800
pasta2 = int(input()) #700
pasta3 = int(input()) #900

juice1 = int(input()) #198
juice2 = int(input()) #330


pasta = [pasta1,pasta2,pasta3]
juice = [juice1,juice2]

minPasta = min(pasta)
minJuice = min(juice)

minSumPrice = minPasta + minJuice
addPrice = minSumPrice * 0.1 #10%

resultPrice = minSumPrice + addPrice

print(format(resultPrice,".1f"))
