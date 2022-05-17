def is_prime(N):
    num = 2
    while num < int(N**0.5) + 1:
        if N % num == 0:
            return False
        num += 1
    return True


def nth_prime(N):
    cur_num = 2
    counter = 0
    while counter < N:
        if is_prime(cur_num):
            counter += 1
        if counter == N:
            return cur_num
        cur_num += 1


def main():
    N = 10001
    res = nth_prime(N)
    print(f"The answer for problem 7 is: {res}")


main()
