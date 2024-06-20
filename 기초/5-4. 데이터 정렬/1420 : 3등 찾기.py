count = int(input())

members = []

for i in range(count):
    members.append(input().split())

members.sort(key=lambda x: int(x[1]))

print(members[2][0])
