n = int(input())
number = list(map(int, input().split()))
ops = list(map(int, input().split()))

min_result = float('inf')
max_result = float('-inf')

op_list = []

def recursive():
    global min_result, max_result

    if len(op_list) == n-1:
        result = number[0]

        for j in range(n-1):
            if op_list[j] == 0:
                result += number[1 + j]
            elif op_list[j] == 1:
                result -= number[1 + j]
            elif op_list[j] == 2:
                result *= number[1 + j]

        if result < min_result: min_result = result
        if result > max_result: max_result = result

        return

    for i in range(3):
        if ops[i] > 0:
            op_list.append(i)
            ops[i] -= 1
            recursive()
            ops[i] += 1
            op_list.pop()

recursive()

print(min_result, max_result)