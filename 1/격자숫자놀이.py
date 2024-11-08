r, c, k = list(map(int, input().split()))
r, c = r - 1, c - 1

arr = [
    list(map(int, input().split()))
    for _ in range(3)
]
n = len(arr)
m = len(arr[0])

t = 0

def sort_line(line):
    cnt_by_num = dict()
    for l in line:
        if l != 0:
            if l in cnt_by_num:
                cnt_by_num[l] += 1
            else:
                cnt_by_num[l] = 1

    num_by_cnt = dict()
    for c in cnt_by_num:
        if cnt_by_num[c] in num_by_cnt:
            num_by_cnt[cnt_by_num[c]].append(c)
        else:
            num_by_cnt[cnt_by_num[c]] = [c]

    sort_cnt = sorted(num_by_cnt.keys(), key=lambda x:x)

    new_line = []
    for cnt in sort_cnt:
        num_list = num_by_cnt[cnt]
        sorted_num_list = sorted(num_list)

        for num in sorted_num_list:
            new_line.extend([num, cnt])
    return new_line

for t in range(102):
    if 0 <= r < n and 0 <= c < m:
        if arr[r][c] == k:
            break

    new_arr = []
    if n < m:
        copy_arr = [
            [-1 for _ in range(n)]
            for _ in range(m)
        ]
        for i in range(n):
            for j in range(m):
                copy_arr[j][i] = arr[i][j]
    else:
        copy_arr = arr


    max_len = 0
    for a in copy_arr:
        new_a = sort_line(a)
        new_arr.append(new_a)
        max_len = max(max_len, len(new_a))

    for i in range(len(new_arr)):
        for _ in range(len(new_arr[i]), max_len):
            new_arr[i].append(0)

    if n < m:
        copy_new_arr = [
            [-1 for _ in range(len(new_arr))]
            for _ in range(len(new_arr[0]))
        ]
        for i in range(len(new_arr)):
            for j in range(len(new_arr[i])):
                copy_new_arr[j][i] = new_arr[i][j]
    else:
        copy_new_arr = new_arr

    arr = copy_new_arr
    n = len(arr)
    m = len(arr[0])

if t > 100:
    print(-1)
else:
    print(t)