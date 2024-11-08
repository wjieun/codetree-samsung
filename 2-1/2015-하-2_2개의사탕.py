from collections import deque
from copy import deepcopy

N, M = list(map(int, input().split()))

mapping = {
    '.': 0,
    '#': 1,
    'B': 2,
    'R': 3,
    'O': -1
}

init_arr = [
    [mapping[s] for s in list(input())]
    for _ in range(N)
]

init_red, init_blue = -1, -1

for i in range(N):
    for j in range(M):
        if init_arr[i][j] == 2:
            init_blue = (i, j)
            init_arr[i][j] = 0
        elif init_arr[i][j] == 3:
            init_red = (i, j)
            init_arr[i][j] = 0

def lean(d, old_red, old_blue):
    red, blue = list(old_red), list(old_blue)

    if d == 0: # 위
        if blue[0] < red[0]:
            ball_list = [blue, red]
        else:
            ball_list = [red, blue]

        for b, ball in enumerate(ball_list):
            j = ball[1]
            for i in range(ball[0]-1, 0, -1):
                if (b == 1 and ball_list[0][0] == i and ball_list[0][1] == j) \
                        or init_arr[i][j] == 1:
                    break
                elif init_arr[i][j] == 0:
                    ball[0] = i
                else:
                    ball[0], ball[1] = -1, -1
                    break

    elif d == 1: # 아래
        if blue[0] > red[0]:
            ball_list = [blue, red]
        else:
            ball_list = [red, blue]

        for b, ball in enumerate(ball_list):
            j = ball[1]
            for i in range(ball[0] + 1, N-1, 1):
                if (b == 1 and ball_list[0][0] == i and ball_list[0][1] == j) \
                        or init_arr[i][j] == 1:
                    break
                elif init_arr[i][j] == 0:
                    ball[0] = i
                else:
                    ball[0], ball[1] = -1, -1
                    break

    elif d == 2: # 왼쪽
        if blue[1] < red[1]:
            ball_list = [blue, red]
        else:
            ball_list = [red, blue]

        for b, ball in enumerate(ball_list):
            i = ball[0]
            for j in range(ball[1]-1, 0, -1):
                if (b == 1 and ball_list[0][0] == i and ball_list[0][1] == j)\
                        or init_arr[i][j] == 1:
                    break
                elif init_arr[i][j] == 0:
                    ball[1] = j
                else:
                    ball[0], ball[1] = -1, -1
                    break

    elif d == 3: # 오른쪽
        if blue[1] > red[1]:
            ball_list = [blue, red]
        else:
            ball_list = [red, blue]

        for b, ball in enumerate(ball_list):
            i = ball[0]
            for j in range(ball[1]+1, M-1, 1):
                if (b == 1 and ball_list[0][0] == i and ball_list[0][1] == j) \
                        or init_arr[i][j] == 1:
                    break
                elif init_arr[i][j] == 0:
                    ball[1] = j
                else:
                    ball[0], ball[1] = -1, -1
                    break

    return tuple(red), tuple(blue)

min_count = 11
for i in range(4):
    visited = set()
    q = deque()
    q.append((i, 1, init_red, init_blue))

    while q:
        now_d, count, now_red, now_blue = q.popleft()
        if count >= min_count:
            break

        new_red, new_blue = lean(now_d, now_red, now_blue)

        if new_blue == (-1, -1):
            continue
        elif new_red == (-1, -1):
            min_count = count
            continue

        if (new_red, new_blue) not in visited:
            visited.add((new_red, new_blue))
            for new_d in range(4):
                q.append((new_d, count + 1, new_red, new_blue))

if min_count == 11:
    print(-1)
else:
    print(min_count)