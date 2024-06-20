"""
버블 정렬 : 인접한 두 원소를 검사하여 자리를 바꿔가며 정렬하는 방식
"""


def bubble_sort(arr):
    n = len(arr)
    # 배열의 모든 요소를 순회
    for i in range(n):
        # 마지막 i 요소는 이미 정렬된 상태이므로 n-i-1까지 검토
        for j in range(0, n-i-1):
            # 현재 요소가 다음 요소보다 크면 두 요소의 위치를 바꿈
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]



count = int(input())
arr = []

for _ in range(count):
    arr.append(int(input()))

bubble_sort(arr)
print(*arr)