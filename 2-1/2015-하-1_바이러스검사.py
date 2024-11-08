n = int(input())
customer = list(map(int, input().split()))
leader_max, member_max = list(map(int, input().split()))

result = n

for i in range(n):
    customer[i] = customer[i] - leader_max
    if customer[i] < 0: customer[i] = 0

    result += customer[i] // member_max
    if customer[i] % member_max != 0:
        result += 1

print(result)