def prod(lst):
    res = 1
    for val in lst:
        res *= val
    return res


def read_data():
    data = []
    with open("data.txt", "r") as fp:
        for line in fp.readlines():
            data.append(list(map(int, list(line.strip("\n").split(" ")))))
    return data


def right_prod(data, N):
    res = 1
    for row in data:
        for i in range(0, len(row) - N + 1):
            res = max(res, prod(row[i : i + N]))
    return res


def left_prod(data, N):
    res = 1
    for row in data:
        row_r = row[::-1]
        for i in range(0, len(row) - N + 1):
            res = max(res, prod(row_r[i : i + N]))
    return res


def diag_prod(data, N):
    res = 1
    for i in range(len(data)):
        for j in range(len(data)):
            idxs = [[i + o, j + o] for o in range(N)]
            if all(i1[0] < len(data) and i1[1] < len(data) for i1 in idxs):
                res = max(res, prod([data[i1[0]][i1[1]] for i1 in idxs]))
    return res


def largest_prod_in_grid(N):
    data = read_data()
    data_r = [row[::-1] for row in data]

    right_ans = right_prod(data, N)
    left_ans = left_prod(data, N)
    down_ans = right_prod(data_r, N)
    up_ans = left_prod(data_r, N)
    diag_1_ans = diag_prod(data, N)
    diag_2_ans = diag_prod(data_r, N)

    return max([right_ans, left_ans, down_ans, up_ans, diag_1_ans, diag_2_ans])


def main():
    N = 4
    res = largest_prod_in_grid(N)
    print(f"The answer for problem 11 is: {res}")


main()
