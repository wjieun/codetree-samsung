n, m = list(map(int, input().split()))

map = [
    list(map(int, input().split()))
    for _ in range(n)
] # 빈칸 0, 사람 1, 병원 2

hospitals = []
people = []
for i in range(n):
    for j in range(n):
        if map[i][j] == 1:
            people.append((i, j))
        elif map[i][j] == 2:
            hospitals.append((i, j))

def get_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def get_dis_sum():
    dis = 0
    for px, py in people:
        min_p_d = float('inf')
        for si in selected:
            sx, sy = hospitals[si]
            p_d = get_distance(sx, sy, px, py)
            if p_d < min_p_d: min_p_d = p_d
        dis += min_p_d
    return dis

selected = []
min_dis = float('inf')
def recursive(idx):
    global min_dis
    if len(selected) == m:
        dis_sum = get_dis_sum()
        if dis_sum < min_dis:
            min_dis = dis_sum
        return

    if idx == len(hospitals):
        return

    recursive(idx + 1)

    selected.append(idx)
    recursive(idx + 1)
    selected.pop()

recursive(0)
print(min_dis)