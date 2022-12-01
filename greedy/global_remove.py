# @Author : Cheng Huang
# @Time   : 11:18 2022/11/25
# @File   : global_remove.py



from scipy.stats import entropy


def global_remove_list(relations, cluster, file):
    '''
    remove the most frequent and the second frequent relation
    :param relation that need to remove
    :param cluster:
    :param file:
    :return:
    '''

    i = -1
    obtain_triple_ids = []
    with open(file, 'r') as f:
        for line in f:
            rel = str(line.split("\t")[1])
            i += 1
            if rel not in relations:
                obtain_triple_ids.append(i)
    f.close()

    obtains_triples = {}

    for i in obtain_triple_ids:
        obtains_triples[i] = entropy(cluster[i])

    obtains_sort = sorted(obtains_triples.items(), key=lambda item: item[1], reverse=True)

    res = []

    for item in obtains_sort:
        res.append(item[0])

    # we first search from the other, then most
    # print("res", res, len(res))

    return len(res), res


