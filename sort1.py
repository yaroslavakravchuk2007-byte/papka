import sys
arr = list(map(int, sys.stdin.readline().split()))
n = len(arr)
is_min_heap = True
for i in range(n // 2):
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] > arr[left]:
        is_min_heap = False
        break

    if right < n and arr[i] > arr[right]:
        is_min_heap = False
        break
print(1 if is_min_heap else 0)
#благодарю моего друга гпт за огромную помощь 