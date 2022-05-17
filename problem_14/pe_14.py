def collatz_length(N):
    l = 1
    while N != 1:
        if N % 2 == 0:
            N = N // 2
        else:
            N = (3 * N) + 1
        l += 1
    return l


def longest_collatz_sequence(N):
    i = 1
    max_len = 1
    res_num = 1
    while i < N:
        cur_res = collatz_length(i)
        if cur_res > max_len:
            max_len = cur_res
            res_num = i
        i += 1
        if i % 100000 == 0:
            print(f"{i} out of {N} completed")
    return res_num


def main():
    N = 1000000
    res = longest_collatz_sequence(N)
    print(f"The answer for problem 14 is: {res}")


main()
