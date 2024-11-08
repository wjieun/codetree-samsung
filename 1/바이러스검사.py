n = int(input())
client_num = list(map(int, input().split()))
max_client_num = list(map(int, input().split()))

def find(c_num):
    global max_client_num

    c_num -= max_client_num[0]
    leader, member = 1, 0

    if c_num > 0:
        member = c_num // max_client_num[1]
        if c_num % max_client_num[1] != 0: member += 1

    return leader + member

cnt = 0
for i in range(n):
    cnt += find(client_num[i])
print(cnt)