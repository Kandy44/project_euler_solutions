def read_data():
    data = []
    with open("data.txt", "r") as fp:
        for line in fp.readlines():
            data.append(int(line.strip("\n")))
    return data


def large_sum():
    l_sum = 0
    data = read_data()
    for num in data:
        l_sum += num
    return l_sum


def main():
    N = 10
    res = str(large_sum())[:N]
    print(f"The answer for problem 13 is: {res}")


main()
