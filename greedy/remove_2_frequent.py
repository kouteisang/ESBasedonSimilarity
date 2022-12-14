# @Author : Cheng Huang
# @Time   : 09:38 2022/11/22
# @File   : remove_2_frequent.py


from scipy.stats import entropy


def remove_top2_frequent(cluster, file):
    '''
    remove the most frequent and the second frequent relation
    :param cluster:
    :param file:
    :return:
    '''
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
    second_rel = rel_count[1][0]
    # print(most_rel)
    i = -1
    most_rel_pos = []
    second_rel_pos = []
    with open(file, 'r') as f:
        for line in f:
            rel = str(line.split("\t")[1])
            i += 1
            if rel == most_rel:
                most_rel_pos.append(i)
            elif rel == second_rel:
                second_rel_pos.append(i)
    f.close()

    # print(most_rel_pos)

    groupother = {}
    groupmost = {}
    groupsecond = {}

    l = cluster.shape[0]
    for i in range(l):
        if i in most_rel_pos:
            groupmost[i] = entropy(cluster[i])
        elif i in second_rel_pos:
            groupsecond[i] = entropy(cluster[i])
        else:
            groupother[i] = entropy(cluster[i])

    res_most = sorted(groupmost.items(), key=lambda item: item[1], reverse=True)
    res_second = sorted(groupsecond.items(), key=lambda item: item[1], reverse=True)
    res_other = sorted(groupother.items(), key = lambda item:item[1], reverse=True)

    # we first search from the other, then most
    print("res_other", file, len(res_other))
    res = []
    for item in res_other:
        res.append(item[0])
    for item in res_second:
        res.append(item[0])
    for item in res_most:
        res.append(item[0])

    return res



def remove_top2_frequent_may_not_k(cluster, file):
    '''
    remove the most frequent and the second frequent relation,
    when the number of stasify triples not equals to k, we just return the stasify triples
    :param cluster:
    :param file:
    :return:
    '''
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
    second_rel = rel_count[1][0]
    # print(most_rel)
    i = -1
    most_rel_pos = []
    second_rel_pos = []
    with open(file, 'r') as f:
        for line in f:
            rel = str(line.split("\t")[1])
            i += 1
            if rel == most_rel:
                most_rel_pos.append(i)
            elif rel == second_rel:
                second_rel_pos.append(i)
    f.close()

    # print(most_rel_pos)

    groupother = {}
    groupmost = {}
    groupsecond = {}

    l = cluster.shape[0]
    for i in range(l):
        if i in most_rel_pos:
            groupmost[i] = entropy(cluster[i])
        elif i in second_rel_pos:
            groupsecond[i] = entropy(cluster[i])
        else:
            groupother[i] = entropy(cluster[i])

    res_most = sorted(groupmost.items(), key=lambda item: item[1], reverse=True)
    res_second = sorted(groupsecond.items(), key=lambda item: item[1], reverse=True)
    res_other = sorted(groupother.items(), key = lambda item:item[1], reverse=True)

    # we first search from the other, then most
    print("res_other", file, len(res_other))
    res = []
    for item in res_other:
        res.append(item[0])
    for item in res_second:
        res.append(item[0])
    for item in res_most:
        res.append(item[0])

    return len(res_other), res
