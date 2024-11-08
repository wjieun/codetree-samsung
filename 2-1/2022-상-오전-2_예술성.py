from collections import deque
from copy import deepcopy

n = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

def in_range(a, b):
    return 0 <= a < n and 0 <= b < n

def get_score():
    visited = [
        [False] * n
        for _ in range(n)
    ]

    groups = []

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                number = arr[i][j]
                group = set()

                q = deque()
                q.append((i, j))
                visited[i][j] = True

                while q:
                    qi, qj = q.popleft()
                    group.add((qi, qj))

                    for dx, dy in zip(dxs, dys):
                        new_x, new_y = qi + dx, qj + dy

                        if in_range(new_x, new_y) and not visited[new_x][new_y]\
                                and arr[new_x][new_y] == number:
                            q.append((new_x, new_y))
                            visited[new_x][new_y] = True

                groups.append((number, group))

    score_sum = 0
    for i in range(len(groups)):
        for j in range(i + 1, len(groups)):
            number1, group1 = groups[i]
            number2, group2 = groups[j]

            score = len(group1) + len(group2)
            score *= number1 * number2

            contact_lines = 0
            for gx, gy in group1:
                for dx, dy in zip(dxs, dys):
                    new_x, new_y = gx + dx, gy + dy
                    if (new_x, new_y) in group2:
                        contact_lines += 1

            score *= contact_lines
            score_sum += score

    return score_sum

def rotate():
    global arr
    mid = n // 2

    new_arr = deepcopy(arr)

    # boxes
    for x in [0, mid + 1]:
        for y in [0, mid + 1]:
            # each box
            for i in range(mid):
                for j in range(mid):
                    new_arr[x + j][y + mid - 1 - i] = arr[x + i][y + j]

    # cross
    for i in range(n):
        for j in range(n):
            if i == mid or j == mid:
                new_arr[n - 1 - j][i] = arr[i][j]

    arr = new_arr


all_score_sum = get_score()
for _ in range(3):
    rotate()
    all_score_sum += get_score()
print(all_score_sum)