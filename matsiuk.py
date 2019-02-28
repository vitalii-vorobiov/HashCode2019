from copy import deepcopy
def file_in(path):
    res_h = []
    res_v = []
    with open(path, "r") as f:
        print(f"n= {f.readline()}")
        counter = 0
        for line in f:
            res_word = line.split()
            if res_word[0] == 'H':
                res_h.append([str(counter), set(res_word[2:])])
            else:
                res_v.append([str(counter), set(res_word[2:])])
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

def get_input(file):
    x,y = file_in(f"in/{file}")
    return x+merge(y)



def score(it1, it2):
    item1 = it1[1]
    item2 = it2[1]
    return min(len(item1.intersection(item2)),len(item1-item2),len(item2-item1))

def chunkIt(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out



inp = get_input("d_pet_pictures.txt")


merged_res=[]
merged_score=0
cnt = 0
for unused in chunkIt(inp, 90):
    overall_res = []
    for first in range(1):
        # unused = deepcopy(inp_file)
        res = []
        res.append(unused.pop(first))

        step_score = 0
        while len(unused) != 0:
            maximum = (-1, -1)
            for i in range(len(unused)):
                current_score = score(res[-1], unused[i])
                if current_score > maximum[1]:
                    maximum = (i, current_score)

            popped_value = unused.pop(maximum[0])
            res.append(popped_value)
            step_score += maximum[1]


        overall_res.append((list(map(lambda x:x[0], res)),step_score))

    result = max(overall_res, key=lambda x:x[1])
    merged_res+=result[0]
    merged_score+=result[1]
    cnt+=1
    print(cnt)



print(merged_score)
