n = int(input())
start = list(map(int, input().split()))
end = list(map(int, input().split()))

meetings = []
for i in range(n):
    meetings.append((start[i], end[i]))

meetings.sort(key=lambda x: x[1])

count = 0
last_end = -1

for s, e in meetings:
    if s > last_end:
        count += 1
        last_end = e

print(count)