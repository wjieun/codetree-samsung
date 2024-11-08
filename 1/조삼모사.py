n = int(input())
P = []
for _ in range(n):
    P.append(list(map(int, input().split())))

min_p = 100000
evening = [False for _ in range(n)]

def get_p():
    morning_sum = sum([
        P[i][j]
        for i in range(n)
        for j in range(n)
        if not evening[i] and not evening[j]
    ])

    evening_sum = sum([
        P[i][j]
        for i in range(n)
        for j in range(n)
        if evening[i] and evening[j]
    ])

    return abs(morning_sum - evening_sum)

def find_min(idx, cnt):
    global min_p

    if cnt == n // 2:
        min_p = min(min_p, get_p())
        return

    if idx == n:
        return

    find_min(idx+1, cnt)

    evening[idx] = True
    find_min(idx+1, cnt+1)
    evening[idx] = False

find_min(0, 0)
print(min_p)