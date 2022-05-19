def distinct_powers(a,b):
    num_set = set()
    for i in range(2,a+1):
        for j in range(2,b+1):
            num_set.add(i**j)
    return len(num_set)

def main():
    a,b=100,100
    res = distinct_powers(a,b)
    print(f"The answer for problem 29 is: {res}")

main()