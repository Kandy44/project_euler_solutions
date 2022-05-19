def is_palindrome(s):
    return s == s[::-1]

def double_base_palindromes(N):
    num_sum = 0
    i = 1
    while i < N:
        if is_palindrome(str(i)) and is_palindrome(bin(i)[2:]):
            num_sum += i
        i += 1
    return num_sum



def main():
    N = 1000000
    res = double_base_palindromes(N)
    print(f"The answer for problem 36 is: {res}")


main()
