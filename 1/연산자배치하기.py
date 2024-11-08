n = int(input())
num_list = list(map(int, input().split()))
operator_list = list(map(int, input().split()))

min_result = float('inf')
max_result = float('-inf')

def calc(num1, num2, op):
    if op == 0: return num1 + num2
    elif op == 1: return num1 - num2
    elif op == 2: return num1 * num2

def append_operator():
    for i in range(3):
        if operator_list[i] > 0:
            selected.append(i); operator_list[i] -= 1
            recursive(i)
            selected.pop(); operator_list[i] += 1

# +(0) -(1) *(2)
selected = []
def recursive(op):
    global min_result, max_result

    if sum(operator_list) == 0:
        result = num_list[0]
        for i in range(1, n):
            result = calc(result, num_list[i], selected[i - 1])
        min_result = min(min_result, result)
        max_result = max(max_result, result)
        return

    if len(selected) == n - 1:
        operator_list[op] += 1
        return

    append_operator()

append_operator()
print(min_result, max_result)