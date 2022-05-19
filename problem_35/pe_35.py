primes = []


def sieve(n):
    # To access the global prime variable
    global primes

    # Updating the value of primes to be an list of boolean values
    # with the initial value being true
    # This list stores if a number is prime or not
    # for numbers [0...n]
    primes = [True for _ in range(n + 1)]
    # Updating first two values to false
    primes[0] = False
    primes[1] = False

    # This is the current number
    curNum = 2

    while curNum * curNum <= n:
        # If current number is prime
        if primes[curNum]:
            # Then we update the values of all it's multiples to be false
            for i in range(curNum**2, n + 1, curNum):
                primes[i] = False
        curNum += 1


def is_circular_prime(n):
    if n < 10:
        return primes[n]
    
    digits = list(str(n))
    c = 0
    
    while c < len(digits):
        if not primes[int(''.join(digits))]:
            return False
        else:
            digits = digits[1:] + [digits[0]]
        c += 1
    return True

def circular_primes_count(N):
    sieve(N - 1)

    i = 3
    l = len(primes)
    count = 1
    while i < l:
        if primes[i]:
            if is_circular_prime(i):
                count += 1
        i += 2
    return count


def main():
    N = 1000000
    res = circular_primes_count(N)
    print(f"The answer for problem 35 is: {res}")


main()
