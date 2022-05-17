def div_sum(n):
    i = 1
    d_sum = 0
    while i < n:
        if n%i==0:
            d_sum += i
        i += 1
    return d_sum

def amicable_numbers(n):
    ans = 0
    d = {i:div_sum(i) for i in range(1,n)}
    for a in range(1,n):
        v1 = d.get(a)
        v2 = d.get(v1,-1)
        if a == v2 and a != v1:
            ans += a
    return ans

def main():
    N = 10000
    res = amicable_numbers(N)
    print(f"The answer for problem 21 is: {res}")

main()