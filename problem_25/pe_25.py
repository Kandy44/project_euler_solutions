def n_digit_fib(N):
    prev, cur = 1, 1
    even_sum = 0
    idx=2
    while len(str(cur)) < N:
        if cur % 2 == 0:
            even_sum += cur
        next_val = prev + cur
        prev = cur
        cur = next_val
        idx += 1
    return idx


def main():
    N = 1000
    res = n_digit_fib(N)
    print(f"The answer for problem 25 is: {res}")

main()