import math

abundant_numbers = []

def divisor_sum(n):
    div_sum = 1
    i = 2
    while i <= math.sqrt(n):
        if n%i==0:
            if i == n//i:
                div_sum += i
            else:
                div_sum += (i + (n // i))
        i += 1
    return div_sum

def calculate_abundant_numbers(limit):
    global abundant_numbers
    i = 1
    while i <= limit:
        if divisor_sum(i) > i:
            abundant_numbers.append(i)
        i += 1
    
def non_abundant_numbers_sum(limit):
    is_expressible = [False] * limit
    for i in abundant_numbers:
        for j in abundant_numbers:
            if i + j < limit:
                is_expressible[i+j] = True
            else:
                break
    return sum(idx for idx,val in enumerate(is_expressible) if not val)

def main():
    N = 28124
    calculate_abundant_numbers(N)
    res = non_abundant_numbers_sum(N)
    print(f"The answer for problem 23 is: {res}")

main()