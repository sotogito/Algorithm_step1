oneBtn = 1

fiveBtn = 5

tenBtn = 10

nowTemperature, targetTemperature = map(int, input().split())

changeTemperature = abs(targetTemperature - nowTemperature)

count = 0

while True:
    if changeTemperature == 0:
        break

    tenBtnCount = int(changeTemperature / tenBtn)
    count += tenBtnCount
    changeTemperature -= tenBtnCount * tenBtn

    if changeTemperature != 0:
        distance_to_0 = abs(changeTemperature - 1)
        distance_to_5 = abs(changeTemperature - 5)
        distance_to_10 = abs(changeTemperature - 10)

        min_distance = min(distance_to_0, distance_to_5, distance_to_10)

        if min_distance == distance_to_0:
            changeTemperature = abs(changeTemperature - oneBtn)
        elif min_distance == distance_to_5:
            changeTemperature = abs(changeTemperature - fiveBtn)
        elif min_distance == distance_to_10:
            changeTemperature = abs(changeTemperature - tenBtn)

        count += 1

        oneBtnCount = int(changeTemperature / oneBtn)
        count += oneBtnCount
        changeTemperature -= oneBtnCount * oneBtn

print(count)

