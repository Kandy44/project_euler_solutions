def tri_num(n):
    return (n * (n + 1)) // 2


def div_count(n):
    sqrt_n = (n + 1) ** 0.5
    res = sum(n % i == 0 for i in range(1, int(sqrt_n) + 1)) * 2
    if sqrt_n**2 == n:
        res -= 1
    return res


def highly_divisible_num(N):
    i = 1
    while True:
        n = tri_num(i)
        if div_count(n) >= N:
            return n
        i += 1


def main():
    N = 500
    res = highly_divisible_num(N)
    print(f"The answer for problem 12 is: {res}")


main()
