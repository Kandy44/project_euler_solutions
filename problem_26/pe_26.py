def cycle_count(n):
    idxs = {}
    i = 0
    s = 1
    while True:
        if s in idxs:
            return i - idxs[s]
        else:
            idxs[s] = i
            s = s*10%n
        i += 1


def main():
    res_num = 0
    res_len = 0
    for i in range(2,1000):
        cur_num_length = cycle_count(i)
        if cur_num_length > res_len:
            res_num = i
            res_len = cur_num_length

    print(f"The answer for problem 26 is: {res_num}")

main()