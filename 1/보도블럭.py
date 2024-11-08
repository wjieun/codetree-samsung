import copy

n, L = list(map(int, input().split()))
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

can_go = 0

def find_can_go(array):
    global can_go

    for row in array:
        slope = [False for _ in range(n)]

        i = 0
        while i < n - 1:
            now, next = row[i], row[i + 1]

            if now == next:
                i += 1
            elif now == next + 1:
                if i + L < n:
                    can_install = True
                    for k in range(L):
                        if row[i + 1 + k] != next or slope[i + 1 + k]:
                            can_install = False
                            break

                    if can_install:
                        for k in range(L):
                            slope[i + 1 + k] = True
                        i += L
                        continue
                break
            elif now + 1 == next:
                if i + 1 - L >= 0:
                    can_install = True
                    for k in range(L):
                        if row[i - k] != now or slope[i - k]:
                            can_install = False
                            break

                    if can_install:
                        for k in range(L):
                            slope[i - k] = True
                        i += 1
                        continue
                break
            else:
                break

        if i == n - 1:
            can_go += 1

new_arr = copy.deepcopy(arr)
find_can_go(new_arr)

for i in range(n):
    for j in range(n):
        new_arr[i][j] = arr[j][i]
find_can_go(new_arr)

print(can_go)