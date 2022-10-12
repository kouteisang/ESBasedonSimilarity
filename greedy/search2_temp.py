# @Author : Cheng Huang
# @Time   : 13:51 2022/10/11
# @File   : search2_temp.py
import numpy as np
from numpy import dot
from numpy.linalg import norm
import networkx

from greedy.desc_value import calculate_desc_value


def cosine_similiarity(x, y):
    '''

    :param x: list e.g. [1,2,3]
    :param y: list e.g. [1,2,3]
    :return: cosine similarity between x and y
    '''
    return dot(x, y)/(norm(x)*norm(y))
    # this is the L1 norm, remember if we use the L1 norm, we need to choose the max
    # return np.linalg.norm((x - y), ord=1)

def greedy_search2(cluster, k, file_path):
    '''
    :param cluster: the fuzzy cluster result
    :param k: top K most different from each other
    :return res: the top K index
    '''
    cnt = 0
    l = cluster.shape[0]
    similarity_all = np.zeros(l*l).reshape((l,l))
    res = []
    max_value = 0

    # calculate the pair-wise similarity between two entity
    for i in range(l):
        for j in range(l):
            similarity_all[i][j] = 1 - cosine_similiarity(cluster[i], cluster[j])

    desc_val = calculate_desc_value(file_path)
    # from this step, we want to get all complete graph
    complete_graph = networkx.complete_graph(l)
    subgraph = networkx.enumerate_all_cliques(complete_graph)


    for g in subgraph:
        if len(g) == k:
            temp_val = 0
            for i in range(k):
                for j in range(i, k):
                    if i == j:
                        temp_val += desc_val[g[i]]
                    else:
                        temp_val += similarity_all[g[i]][g[j]]
            if temp_val >  max_value:
                max_value = temp_val
                res = g
        if len(g) > k:
            break

    return res



