h, m = map(int, input().split())

# 1시간은 60분임을 정의
change_time_minutes = 30

# 분에서 변경할 시간을 빼기
m -= change_time_minutes

# 분이 음수가 되면 시간을 조정
if m < 0:
    m += 60  # 음수 분을 조정하여 60분을 더함
    h -= 1  # 시간에서 1시간을 빼줌

# 시간이 음수가 되면 24시간제를 고려하여 조정
if h < 0:
    h += 24

print(h, m)
