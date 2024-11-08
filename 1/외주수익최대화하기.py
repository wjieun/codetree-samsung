n = int(input())
time = []
profit = []
max_p = 0

for i in range(n):
    work = list(map(int, input().split()))
    time.append([i, i + work[0] - 1])
    profit.append(work[1])

selected = list()
def recursive(day):
    global max_p

    if day == n:
        is_available = True
        for i in range(len(selected)):
            if i < len(selected) - 1:
                if time[selected[i]][1] >= time[selected[i+1]][0]:
                    is_available = False
            if time[selected[i]][1] >= n:
                is_available = False

        if is_available:
            p_sum = 0
            for i in range(len(selected)):
                p_sum += profit[selected[i]]
            max_p = max(max_p, p_sum)
        return

    recursive(day + 1)

    selected.append(day)
    recursive(day + 1)
    selected.pop()

recursive(0)
print(max_p)