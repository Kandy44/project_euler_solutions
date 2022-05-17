def first_n_multiples_sum(n, m):
    return m * ((n * (n + 1)) // 2)


def multiples_sum(N):
    three_multiples_sum = first_n_multiples_sum((N - 1) // 3, 3)
    five_multiples_sum = first_n_multiples_sum((N - 1) // 5, 5)
    fifteen_multiples_sum = first_n_multiples_sum((N - 1) // 15, 15)
    return (three_multiples_sum + five_multiples_sum) - fifteen_multiples_sum


def main():
    N = 1000
    res = multiples_sum(N)
    print(f"The answer for problem 1 is: {res}")


main()
