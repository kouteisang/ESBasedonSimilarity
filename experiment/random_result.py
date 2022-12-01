# @Author : Cheng Huang
# @Time   : 17:56 2022/12/1
# @File   : random_result.py
import os

from greedy.random_generate import random_generate_res


def get_total_number(path):
    tot = 0
    with open(path, 'r') as f:
        for line in f:
            tot += 1
    f.close()
    return tot

def get_most_frequent_list(path):
    count = {}
    most_frequent_list = []
    with open(path, 'r') as f:
        for line in f:
            s, p, o = line.split("\t")
            if p not in count:
                count[p] = 1
            else:
                count[p] += 1
    count = sorted(count.items(), key=lambda item: item[1], reverse=True)
    res_most = count[0][0]
    if res_most == 'actor':
        if count[0][1] == count[1][1] and count[1][0] == 'performance':
            res_most = 'performance'

    num = -1
    with open(path, 'r') as f:
        for line in f:
            num += 1
            s, p, o = line.split("\t")
            if p == res_most:
                most_frequent_list.append(num)

    return most_frequent_list

def store(top_k, type, id, name, number, len):
    root = os.path.abspath(os.path.dirname(os.getcwd()))+"/ESBasedonSimilarity/"
    folder_name = "random_{}".format(number)
    folder_path = os.path.join(root, "res_data", folder_name, name)
    folder = os.path.exists(folder_path)
    if not folder:
        os.makedirs(folder_path)
    if not os.path.exists(os.path.join(folder_path, str(id))):
        os.makedirs(os.path.join(folder_path, str(id)))

    file_origin = os.path.join(root, "data", name+"_data", str(id), "{}_desc.nt".format(id))

    if type == "top":
        res_path = os.path.join(folder_path, str(id),"{}_top{}.nt".format(id, len))
    if type == "rank":
        file_origin_list = []
        res_path = os.path.join(folder_path, str(id), "{}_rank.nt".format(id))
        with open(file_origin, 'r') as f:
            for line in f:
                line = line[:-1]
                file_origin_list.append(line)
        res = open(res_path, 'w')
        for ele in top_k:
            res.write(file_origin_list[ele]+'\n')
        res.close()
        f.close()
        return

    res = open(res_path, 'w')
    cnt = -1
    with open(file_origin, 'r') as f:
        for line in f:
            cnt = cnt + 1
            line = line[:-1]
            if cnt in top_k:
                res.write(line+'\n')
    res.close()
    f.close()



def random_generate(name, number):
    """
    :param k: number of cluster, hyperparameter
    :return:
    """
    root = os.path.abspath(os.path.dirname(os.getcwd())) + "/ESBasedonSimilarity/"
    if name == "lmdb":
        file_base = os.path.join(root,"data_analysis", "lmdb")
        file_path = []
        for i in range(101,141):
            file_path.append({os.path.join(file_base,"{}_desc.nt".format(i)):i})
        for i in range(166, 176):
            file_path.append({os.path.join(file_base,"{}_desc.nt".format(i)):i})

    if name == "dbpedia":
        file_base = os.path.join(root,"data_analysis", "dbpedia")
        file_path = []
        for i in range(1,101):
            file_path.append({os.path.join(file_base,"{}_desc.nt".format(i)):i})
        for i in range(141, 166):
            file_path.append({os.path.join(file_base,"{}_desc.nt".format(i)):i})


    for file in file_path:
        key = list(file)[0]  # file path
        value = file[key]  # id
        tot = get_total_number(key)
        most_frequent_list = get_most_frequent_list(key)
        t_res = random_generate_res(tot, 10, most_frequent_list)
        top_5 = min(5 , len(t_res))
        store(t_res[:top_5], "top", value, name, number, 5)
        top_10 = min(10, len(t_res))
        store(t_res[:top_10], "top", value, name, number, 10)