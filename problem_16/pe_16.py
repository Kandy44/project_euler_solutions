def power_digit_sum(N):
    res = 0
    num = 2**N
    while num > 0:
        res += (num%10)
        num = num//10
    return res

def main():
    N = 1000
    res = power_digit_sum(N)
    print(f"The answer for problem 16 is: {res}")


main()