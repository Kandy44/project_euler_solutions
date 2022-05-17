def largest_prime_factor(N):
    cur_num = 2
    res = 0
    while N > 1:
        if N % cur_num == 0:
            res = max(res, cur_num)
            N /= cur_num
        else:
            cur_num += 1
    return res


def main():
    N = 600851475143
    res = largest_prime_factor(N)
    print(f"The answer for problem 3 is: {res}")


main()
