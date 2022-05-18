from math import factorial

def combinations_count(n,r):
    a = factorial(n)
    b = factorial(r)
    c = factorial(n-r)
    return a//(b * c)

def main():
    N = 20
    res = combinations_count(N*2,N)
    print(f"The answer for problem 15 is: {res}")

main()