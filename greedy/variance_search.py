# @Author : Cheng Huang
# @Time   : 22:04 2022/10/11
# @File   : variance_search.py
import statistics

def cluster_variance(cluster, k):
    '''
    :param cluster: the fuzzy cluster result
    :param k: top K most different from each other
    :return res: the top K index
    '''

    l = cluster.shape[0]
    res = []
    res_dict = {}
    for i in range(l):
        res_dict[i] = statistics.variance(cluster[i])

    sort_dict = sorted(res_dict.items(), key = lambda item:item[1])
    for item in sort_dict:
        res.append(item[0])

    return res

