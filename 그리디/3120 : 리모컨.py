oneBtn = 1

fiveBtn = 5

tenBtn = 10

nowTemperature, targetTemperature = map(int, input().split())

changeTemperature = targetTemperature - nowTemperature
if changeTemperature < 0:
    changeTemperature = -changeTemperature

tenBtnCount = int(changeTemperature / tenBtn)
changeTemperature -= tenBtnCount * tenBtn

fiveBtnCount = int(changeTemperature / fiveBtn)
changeTemperature -= fiveBtnCount * fiveBtn

oneBtnCount = int(changeTemperature / oneBtn)
changeTemperature -= oneBtnCount * oneBtn

count = tenBtnCount + fiveBtnCount + oneBtnCount

print(count)
