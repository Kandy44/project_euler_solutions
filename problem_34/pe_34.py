from math import factorial


def digit_factorials():
    d = {i: factorial(i) for i in range(10)}
    cur_num = 10
    res = 0
    counter = 0
    while counter < 2:
        if cur_num == sum(d[int(digit)] for digit in str(cur_num)):
            res += cur_num
            counter += 1
        cur_num += 1
    return res


def main():
    res = digit_factorials()
    print(f"The answer for problem 34 is: {res}")


main()
