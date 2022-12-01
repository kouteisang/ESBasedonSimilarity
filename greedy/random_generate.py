# @Author : Cheng Huang
# @Time   : 18:04 2022/12/1
# @File   : random_generate.py
import random

def random_generate_res(tot, k, most_frequent):

    indexs = []
    for i in range(tot):
        if i in most_frequent:
            continue
        else:
            indexs.append(i)
    lindexs = len(indexs)
    k = min(len(indexs), k)
    res = []
    while len(res) < k:
        index = random.randint(0, lindexs-1)
        if indexs[index] not in res:
            res.append(indexs[index])
    return res