peak_season, number_of_room = map(int, input().split())
room_schedule = []

#예약 가능한 방을 index로 변환하여 저장
for _ in range(peak_season):
    row =[]
    row = input().strip()
    available_room_index = []
    for index, status in enumerate(row):
        if status == 'O':
            available_room_index.append(index)
    room_schedule.append(available_room_index)

checkIN, checkOut = map(int,input().split())
#예약한 범위의 방 스캐줄만 가져옴
room_schedule = room_schedule[checkIN-1 : checkOut]

is_unable_reservation = False #예약이 불가능할 때
isMove = True # 방을 바꾸지 않아도 될때 = 원래의 방 크기가 똑같을때 eln(room_schedule)
move_count = 0 #공통되는게 없을 때 = 1
now_duplicate_room = room_schedule

#만약 예약이 불가능한 걍우
for i in range(len(room_schedule)-2) :
    if room_schedule[i] == []:
        is_unable_reservation = True

while True :
    before_duplicate_room = []
    move_count += 1
    for i in range(len(now_duplicate_room)-1) :
        #print("지금 펜션")
        #print(now_duplicate_room)

        set1 = set(now_duplicate_room[i]) # []면 안됨
        set2 = set(now_duplicate_room[i+1])

        if not set1 :
            isMove = False
            result = now_duplicate_room[i+1]
            before_duplicate_room.append(result)
            continue

        result = list(set1&set2)
        before_duplicate_room.append(result)
    if all(x == [] for x in before_duplicate_room) :
        break
    now_duplicate_room = before_duplicate_room

room_schedule_result = [item for item in now_duplicate_room if item]

if is_unable_reservation == True:
    print(-1)
elif now_duplicate_room == [] :
    print(0)
elif len(now_duplicate_room) == len(room_schedule) : #공통된 방이 없을 떄 = 다 바꿔야할 때
    print(len(room_schedule)) #아니면 -1
else:
    print(len(room_schedule_result))





