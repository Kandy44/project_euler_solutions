def pythagorean_triplet_prod(n):
    l = n // 2
    i = l
    while i >= 1:
        j = l
        while j >= 1:
            a, b = i, j
            c = n - (a + b)
            if a < b < c and (a + b + c) == n and (a**2 + b**2) == c**2:
                return a * b * c
            j -= 1
        i -= 1


def main():
    N = 1000
    res = pythagorean_triplet_prod(N)
    print(f"The answer for problem 9 is: {res}")


main()
