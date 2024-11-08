n, k = list(map(int, input().split()))
stability = list(map(int, input().split()))
people = [False] * 2 * n
count = 0

while True:
    count += 1

    # 1
    stability.insert(0, stability.pop())
    people.insert(0, people.pop())
    people[n - 1] = False

    # 2
    for i in range(n-2, -1, -1):
        if people[i] and not people[i + 1] and stability[i + 1]:
            people[i + 1] = True
            people[i] = False
            stability[i + 1] -= 1
            people[n - 1] = False

    # 3
    if not people[0] and stability[0]:
        people[0] = True
        stability[0] -= 1

    # 4
    if stability.count(0) >= k:
        break

print(count)