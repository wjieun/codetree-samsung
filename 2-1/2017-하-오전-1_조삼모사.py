n = int(input())
P = [
    list(map(int, input().split()))
    for _ in range(n)
]

def get_strength(works):
    strength = 0
    for w1 in works:
        for w2 in works:
            strength += P[w1][w2]
    return strength

morning = []
min_strength = float('inf')

def recursive(idx):
    global min_strength

    if len(morning) >= n/2:
        s1 = get_strength(morning)
        s2 = get_strength([i for i in range(n) if i not in morning])
        s = abs(s1 - s2)

        if s < min_strength:
            min_strength = s
        return

    if idx >= n:
        return

    recursive(idx + 1)

    morning.append(idx)
    recursive(idx + 1)
    morning.pop()

recursive(0)

print(min_strength)