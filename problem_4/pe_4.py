def is_palindrome(cur_num):
    p = str(cur_num)
    return p == p[::-1]


def largest_palindrome_product(a, b):
    res = 0
    i = a
    while i < b:
        j = a
        while j < b:
            cur_num = i * j
            if is_palindrome(cur_num):
                res = max(res, cur_num)
            j += 1
        i += 1
    return res


def main():
    a, b = 100, 1000
    res = largest_palindrome_product(a, b)
    print(f"The answer for problem 4 is: {res}")


main()
