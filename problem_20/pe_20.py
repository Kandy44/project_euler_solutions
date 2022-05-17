from math import factorial

def digit_sum(n):
    return sum(map(int,list(str(n))))

def factorial_sum(n):
    return digit_sum(factorial(n))

def main():
    N = 100
    res = factorial_sum(N)
    print(f"The answer for problem 20 is: {res}")

main()