from num2words import num2words
def letter_count(n):
    res = sum([len(''.join(i for i in num2words(i) if i.isalpha())) for i in range(1,n+1)])
    return res


def main():
    N = 1000
    res = letter_count(N)
    print(f"The answer for problem 17 is: {res}")

main()