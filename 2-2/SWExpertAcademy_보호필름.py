# import sys
# sys.stdin = open("input.txt", "r")

def check(array):
    if K == 1:
        return True

    for j in range(W):
        valid = False
        for i in range(D - K + 1):
            valid_line = True
            number = array[i][j]
            for x in range(i + 1, i + K):
                if array[x][j] != number:
                    valid_line = False
                    break

            if valid_line:
                valid = True
                break

        if not valid:
            return False

    return True

def recursive(idx, array, count):
    global max_count

    if check(array):
        max_count = count
        return

    if count >= max_count - 1:
        return

    if idx == D:
        return

    for num in range(2):
        if num != num_arr[idx]:
            orig_d = array[idx].copy()
            array[idx] = num_list[num]

            recursive(idx + 1, array, count + 1)

            array[idx] = orig_d

    recursive(idx + 1, array, count)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    D, W, K = list(map(int, input().split()))

    arr = [
        list(map(int, input().split()))
        for _ in range(D)
    ]

    num_arr = [-1] * D
    for d in range(D):
        if all(arr[d]): num_arr[d] = 1
        elif not any(arr[d]): num_arr[d] = 0

    num_list = [[0] * W, [1] * W]

    max_count = K
    recursive(0, arr, 0)

    print(f'#{test_case} {max_count}')
    # ///////////////////////////////////////////////////////////////////////////////////
