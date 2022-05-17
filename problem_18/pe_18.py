def read_data():
    data = []
    with open('data.txt','r') as f:
        for line in f.readlines():
            data.append(list(map(int,line.strip('\n').split(' '))))
    return data

def max_path_sum():
    data = read_data()
    n = len(data)
    i = n-2
    while i >= 0:
        j = 0
        while j <= i:
            data[i][j] += max(data[i+1][j],data[i+1][j+1])
            j+=1
        i -= 1
    return data[0][0]

def main():
    res = max_path_sum()
    print(f"The answer for problem 18 is: {res}")

main()