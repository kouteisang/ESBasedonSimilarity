# @Author : Cheng Huang
# @Time   : 11:32 2022/10/19
# @File   : entropy_search.py
from scipy.stats import entropy

def cluster_entropy(cluster):
    '''
    :param cluster: the fuzzy cluster result
    :return res: the top K index
    '''
    l = cluster.shape[0]
    res = []
    res_dict = {}
    for i in range(l):
        res_dict[i] = entropy(cluster[i])

    sort_dict = sorted(res_dict.items(), key = lambda item:item[1], reverse=True)
    for item in sort_dict:
        res.append(item[0])

    return res
