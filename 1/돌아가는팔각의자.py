# 북(0) 남(1)
arr = [
    list(map(int,list(input())))
    for _ in range(4)
]

k = int(input())
rotate_list = [
    # 번호 n, 방향 d (시계 1, 반시계 -1)
    list(map(int, input().split()))
    for _ in range(k)
]

def do_rotate(r_list):
    r_n, r_d = r_list
    if r_d == 1:
        arr[r_n].insert(0, arr[r_n].pop())
    else:
        new_a = arr[r_n][1:].copy()
        new_a.append(arr[r_n][0])
        arr[r_n] = new_a

for rotate in rotate_list:
    n, d = rotate
    n = n - 1

    to_rotate = [[n, d]]
    for i in range(n, 0, -1):
        if arr[i][6] != arr[i-1][2]:
            new_d = 0
            if abs(i-n) % 2 == 0:
                new_d = -1 if d == 1 else 1
            else:
                new_d = 1 if d == 1 else -1
            to_rotate.append([i-1, new_d])
        else:
            break
    for i in range(n, 3, 1):
        if arr[i][2] != arr[i+1][6]:
            new_d = 0
            if abs(i-n) % 2 == 0:
                new_d = -1 if d == 1 else 1
            else:
                new_d = 1 if d == 1 else -1
            to_rotate.append([i+1, new_d])
        else:
            break

    for r in to_rotate:
        do_rotate(r)

south_sum = 0
for i in range(len(arr)):
    south_sum += arr[i][0] * (2**i)
print(south_sum)