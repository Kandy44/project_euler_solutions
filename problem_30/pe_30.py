def is_power_sum(n,p):
    return n == sum(int(d)**p for d in str(n))

def nth_digit_nums_sum(n):
    ans = 0
    l=10
    r=10**(n+1)
    for i in range(l,r):
        if is_power_sum(i,n):
            ans += i
    return ans

def main():
    n = 5
    res = nth_digit_nums_sum(n)
    print(f"The answer for problem 29 is: {res}")

main()