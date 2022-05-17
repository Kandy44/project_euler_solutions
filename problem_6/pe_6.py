def sum_of_squares(N):
    return (N * (N + 1) * (2 * N + 1)) // 6


def square_of_sum(N):
    return ((N * (N + 1)) // 2) ** 2


def sum_and_squares_diff(N):
    return square_of_sum(N) - sum_of_squares(N)


def main():
    N = 100
    res = sum_and_squares_diff(N)
    print(f"The answer for problem 6 is: {res}")


main()
