n, k = list(map(int, input().split()))
safety_list = list(map(int, input().split()))
person_list = [False for _ in range(len(safety_list))]

stop_time = 0

def new_step():
    global stop_time
    safety_list.insert(0, safety_list.pop())
    person_list.insert(0, person_list.pop())

    person_list[n - 1] = False
    for i in range(n - 2, 0, -1):
        if person_list[i] and not person_list[i + 1] and safety_list[i + 1] > 0:
            person_list[i] = False
            person_list[i + 1] = True
            safety_list[i + 1] -= 1
    person_list[n - 1] = False

    if safety_list[0] > 0 and not person_list[0]:
        person_list[0] = True
        safety_list[0] -= 1

    stop_time += 1

while True:
    if safety_list.count(0) >= k:
        break
    new_step()

print(stop_time)