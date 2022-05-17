def prod(lst):
    res = 1
    for val in lst:
        res *= val
    return res


def read_data():
    data = []
    with open("data.txt", "r") as fp:
        for line in fp.readlines():
            data.extend(list(map(int, list(line.strip("\n")))))
    return data


def largest_adjacent_product(N):
    num = read_data()
    res = 1
    for i in range(0, len(num) - N + 1):
        res = max(res, prod(num[i : i + N]))
    return res


def main():
    N = 13
    res = largest_adjacent_product(N)
    print(f"The answer for problem 8 is: {res}")


main()
