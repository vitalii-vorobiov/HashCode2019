def file_in(path):
    res_h = []
    res_v = []
    with open(path, "r") as f:
        print(f"n= {f.readline()}")
        counter = 0
        for line in f:
            res_word = line.split()
            if res_word[0] == 'H':
                res_h.append((counter, set(res_word[2:])))
            else:
                res_v.append((counter, set(res_word[2:])))
            counter+=1
    # print(len(res))
    return res_h, res_v


def item_merge(it1, it2):
    return f"{it1[0]} {it2[0]}", it1[1].union(it2[1])

def merge(lst):
    res=[]
    for i in range(0, len(lst),2):
        res.append(item_merge(lst[i],lst[i+1]))
    return res


x,y = file_in("in/a_example.txt")
print("h",x)
print("v", merge(y))