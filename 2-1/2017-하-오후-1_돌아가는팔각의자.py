seat = [
    list(map(int, list(input())))
    for _ in range(4)
] # 2, 6
k = int(input())

for _ in range(k):
    n, d = list(map(int, input().split())) # d: 1 시계, -1 반시계
    n = n - 1
    rotate = [(n, d)]

    new_d = d
    for i in range(n, 0, -1):
        if seat[i][6] != seat[i - 1][2]:
            new_d = -new_d
            rotate.append((i - 1, new_d))
        else:
            break

    new_d = d
    for i in range(n, 3):
        if seat[i][2] != seat[i + 1][6]:
            new_d = -new_d
            rotate.append((i + 1, new_d))
        else:
            break

    for r_n, r_d in rotate:
        if r_d == 1:
            seat[r_n].insert(0, seat[r_n].pop())
        elif r_d == -1:
            seat[r_n].append(seat[r_n].pop(0))

result = 0
for i in range(4):
    result += seat[i][0] * (2**i)
print(result)