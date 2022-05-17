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


def prime_sum(N):
    sieve(N - 1)
    i = 3
    l = len(primes)
    res = 2
    while i < l:
        if primes[i]:
            res += i
        i += 2
    return res


def main():
    N = 2000000
    res = prime_sum(N)
    print(f"The answer for problem 10 is: {res}")


main()
