def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return (a // gcd(a, b)) * b


def smallest_multiple(N):
    res = 1
    cur_num = 1
    while cur_num <= N:
        res = lcm(res, cur_num)
        cur_num += 1
    return res


def main():
    N = 20
    res = smallest_multiple(N)
    print(f"The answer for problem 5 is: {res}")


main()
