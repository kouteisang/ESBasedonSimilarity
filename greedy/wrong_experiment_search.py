# @Author : Cheng Huang
# @Time   : 10:18 2022/11/14
# @File   : wrong_experiment.py
import os

from scipy.stats import entropy


def wrong_cluster_entropy(cluster, file):
    rel_count = {}
    with open(file, 'r') as f:
        for line in f:
            rel = line.split("\t")[1]
            if rel not in rel_count:
                rel_count[rel] = 1
            else:
                rel_count[rel] = rel_count[rel] + 1
    f.close()
    rel_count = sorted(rel_count.items(), key=lambda item: item[1], reverse=True)
    most_rel = rel_count[0][0]
    # print(most_rel)
    i = -1
    most_rel_pos = []
    with open(file, 'r') as f:
        for line in f:
            rel = str(line.split("\t")[1])
            i += 1
            if rel == most_rel:
                most_rel_pos.append(i)
    f.close()

    # print(most_rel_pos)

    groupother = {}
    groupmost = {}

    l = cluster.shape[0]
    for i in range(l):
        if i in most_rel_pos:
            groupmost[i] = entropy(cluster[i])
        else:
            groupother[i] = entropy(cluster[i])

    res_most = sorted(groupmost.items(), key=lambda item: item[1], reverse=True)
    res_other = sorted(groupother.items(), key = lambda item:item[1], reverse=True)

    # we first search from the other, then most

    res = []
    for item in res_other:
        res.append(item[0])
    for item in res_most:
        res.append(item[0])

    return res