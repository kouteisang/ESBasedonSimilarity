# @Author : Cheng Huang
# @Time   : 14:10 2022/9/19
# @File   : greedy_search.py
import numpy
import numpy as np
from numpy import dot
from numpy.linalg import norm

def cosine_similiarity(x, y):
    '''

    :param x: list e.g. [1,2,3]
    :param y: list e.g. [1,2,3]
    :return: cosine similarity between x and y
    '''
    return dot(x, y)/(norm(x)*norm(y))
    # this is the L1 norm, remember if we use the L1 norm, we need to choose the max
    # return np.linalg.norm((x - y), ord=1)

def greedy_search(cluster, k):
    '''
    :param cluster: the fuzzy cluster result
    :param k: top K most different from each other
    :return res: the top K index
    '''
    cnt = 0
    l = cluster.shape[0]
    similarity_all = np.zeros(l*l).reshape((l,l))
    res = []
    # calculate the pair-wise similarity between two entity
    for i in range(l):
        for j in range(l):
            similarity_all[i][j] = cosine_similiarity(cluster[i], cluster[j])
    similar = [0]*l
    # find the one that the most disimilary to all of other data points
    for i in range(l):
        for j in range(l):
            if i == j:
                continue
            similar[i] += similarity_all[i][j]

    index = np.argmin(similar)
    res.append(index)
    cnt += 1

    # greedy loop to find the top k-1
    while cnt < k:
        tmp = {}
        for i in range(l):
            # check if i in res, if i already in l just continue
            if i in res:
                continue
            sim = 0
            for j in range(cnt):
                sim += similarity_all[i][res[j]]
            tmp[i] = sim
        index = sorted(tmp.items(), key=lambda item: item[1])[0][0]
        res.append(index)
        cnt = cnt + 1

    return res

