# @Author : Cheng Huang
# @Time   : 09:43 2022/10/11
# @File   : desc_value.py
import numpy as np


def calculate_desc_value(file):
    f = open(file,'r')
    head = {}
    rel = {}
    tail = {}
    total = 0
    descs = []
    for line in f:
        total += 1
        h, r, t = line.split("\t")
        descs.append((h,r,t))
        if h not in head:
            head[h] = 1
        elif h in head:
            head[h] += 1
        if r not in rel:
            rel[r] = 1
        elif r in rel:
            rel[r] += 1
    f.close()
    head = {k:v for k, v in sorted(head.items(), key = lambda item:item[1], reverse=True)}
    true_head = list(head.keys())[0]

    f = open(file,'r')
    val = []
    for line in f:
        h, r, t = line.split("\t")
        if h == true_head:
            if t not in tail:
                tail[t] = 1
            else:
                tail[t] += 1
        if t == true_head:
            if h not in tail:
                tail[h] = 1
            else:
                tail[h] += 1

    for desc in descs:
        h, r, t = desc
        if h == true_head:
            val.append(np.log(total/rel[r])*np.log(1+tail[t]))
        elif t == true_head:
            val.append(np.log(1+ (total/rel[r])*tail[h] ))

    return val

if __name__ == '__main__':
    val = calculate_desc_value("/Users/huangcheng/Documents/ESBasedonSimilarity/data_analysis/dbpedia/70_desc.nt")
    print(val)

