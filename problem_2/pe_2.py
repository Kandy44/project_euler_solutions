def fib_sum(N):
    prev, cur = 1, 1
    even_sum = 0
    while cur < N:
        if cur % 2 == 0:
            even_sum += cur
        next_val = prev + cur
        prev = cur
        cur = next_val
    return even_sum


def main():
    N = 4000000
    res = fib_sum(N)
    print(f"The answer for problem 2 is: {res}")


main()
