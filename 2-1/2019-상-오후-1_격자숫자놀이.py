from collections import defaultdict

r, c, k = list(map(int, input().split()))
r, c = r - 1, c - 1

arr = [
    list(map(int, input().split()))
    for _ in range(3)
]

for count in range(102):
    row_len, col_len = len(arr), len(arr[0])

    if 0 <= r < row_len and 0 <= c < col_len and arr[r][c] == k:
        break

    new_col_len = 0
    new_arr = []

    # 1
    if row_len >= col_len:
        for i in range(row_len):
            sorted_row = defaultdict(lambda: 0)
            for j in range(col_len):
                if arr[i][j] > 0:
                    sorted_row[arr[i][j]] += 1
            sorted_row = sorted(sorted_row.items(), key=lambda x: (x[1], x[0]))

            new_row = []
            for s in sorted_row:
                new_row.extend(s)

            new_arr.append(new_row)
            new_col_len = max(len(new_row), new_col_len)

        for row in new_arr:
            row.extend([0] * (new_col_len - len(row)))

        arr = new_arr

    # 2
    else:
        for j in range(col_len):
            sorted_row = defaultdict(lambda: 0)
            for i in range(row_len):
                if arr[i][j] > 0:
                    sorted_row[arr[i][j]] += 1
            sorted_row = sorted(sorted_row.items(), key=lambda x: (x[1], x[0]))

            new_row = []
            for s in sorted_row:
                new_row.extend(s)

            new_arr.append(new_row)
            new_col_len = max(len(new_row), new_col_len)

        for row in new_arr:
            row.extend([0] * (new_col_len - len(row)))

        row_len = len(new_arr)

        arr = [[0] * row_len for _ in range(new_col_len)]

        for i in range(row_len):
            for j in range(new_col_len):
                arr[j][i] = new_arr[i][j]

if count == 101:
    print(-1)
else:
    print(count)