def file_in(path):
    res = []
    with open(path, "r") as f:
        print(f"n= {f.readline()}")
        for line in f:
            res_v = line.split()
            res.append((res_v[0], set(res_v[2:])))
    print(len(res))
    return res

x = file_in("in/a_example.txt")
# print(x)