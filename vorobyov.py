def read_file(file_name):

    lst = []

    with open(file_name, "r") as f:
        number = int(f.readline())

        for i in range(number):
            a = f.readline().strip().split()
            lst.append([a[0], a[1], a[2:]])

    return lst


if __name__ == '__main__':
    print(read_file("in/a_example.txt"))
