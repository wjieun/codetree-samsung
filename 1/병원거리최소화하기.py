n, m = list(map(int, input().split()))
arr = []

hospital_set = []
people_set = []
selected = set()
min_distance = float('inf')

for i in range(n):
    arr.append(list(map(int, input().split())))
    for j in range(n):
        if arr[i][j] == 1:
            people_set.append((i, j))
        elif arr[i][j] == 2:
            hospital_set.append((i, j))

def min_hospital_distance(ppl):
    min_dis = float('inf')
    for s in selected:
        dis = abs(ppl[0] - s[0]) + abs(ppl[1] - s[1])
        min_dis = min(min_dis, dis)
    return min_dis

def find(idx):
    global min_distance

    if len(selected) == m:
        dis_sum = 0
        for p in people_set:
            dis_sum += min_hospital_distance(p)
        min_distance = min(min_distance, dis_sum)
        return

    if idx == len(hospital_set):
        return

    find(idx+1)

    selected.add(hospital_set[idx])
    find(idx+1)
    selected.remove(hospital_set[idx])

find(0)

print(min_distance)