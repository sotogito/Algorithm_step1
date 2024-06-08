number_of_topping = int(input())

dough_price, topping_price = map(int, input().split())

dough_cal = int(input())
toppings_cal = []

for _ in range(number_of_topping):
    cal = int(input())
    toppings_cal.append(cal)

sorted_toppings_cal = sorted(toppings_cal, reverse=True)

best_pizza_cal = dough_cal
best_pizza_price = dough_price

now_pizza_cal = dough_cal
now_pizza_price = dough_price

#best_pizza_result = best_pizza_cal / best_pizza_price

for sorted_cal in sorted_toppings_cal:

    best_pizza_price = now_pizza_price
    best_pizza_cal = now_pizza_cal

    now_pizza_cal += sorted_cal
    now_pizza_price += topping_price

    best_pizza_result = best_pizza_cal // best_pizza_price
    now_pizza_result = now_pizza_cal // now_pizza_price

    if best_pizza_result > now_pizza_result:
        break


print(best_pizza_result)








"""
최고의 피자 : 1달러당 열량 최대가 되는 피자
1달러당 열량 : 피자 칼로리 / 가

1. 토핑을 내림차순으로 정렬
2. 하나씩 더한 피자값 생성
3. 그에 따른 피자 가격 생성
4. 1달러당 열량 구함
5. 만약 n+1이 n보다 열량이 작다면 그먄 구함


"""
