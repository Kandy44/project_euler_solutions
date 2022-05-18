from itertools import permutations

def nth_perm(n,r):
    d = list(range(r))
    idx = 0
    p = list(permutations(d))
    while True:
        if idx==n-1:
            return ''.join(map(str,p[idx]))
        idx += 1


def main():
    N = 1000000
    r = 10
    res = nth_perm(N, r)
    print(f"The answer for problem 24 is: {res}")

main()