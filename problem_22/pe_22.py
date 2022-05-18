def read_data():
    data = None
    with open('names.txt','r') as fp:
        data = [name.replace('"','') for name in fp.readline().strip('\n').split(',')]
    return data

def names_score():
    names = read_data()
    sorted_names = sorted(names)
    res = 0
    for name in names:
        idx = sorted_names.index(name)+1
        name_worth = sum(ord(i)-ord('A')+1 for i in name)
        res += (name_worth * idx)
    return res


def main():
    res = names_score()
    print(f"The answer for problem 22 is: {res}")

main()