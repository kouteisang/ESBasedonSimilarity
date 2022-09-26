# @Author : Cheng Huang
# @Time   : 11:33 2022/9/26
# @File   : write_result.py
import os

import torch
from pykeen.triples import TriplesFactory
from greedy.greedy_search import greedy_search
from embedding.get_embedding import get_embedding_representation
from soft_clustering.fuzzy_k_means import FCM



def store(top_k, file_path, id, k, m, name):
    root = os.path.abspath(os.path.dirname(os.getcwd()))
    folder_name = name + "_k_" + str(k) + "_m_" + str(m)
    folder_path = os.path.join(root, "res_data", folder_name)
    folder = os.path.exists(folder_path)
    file_origin = os.path.join(root, "data", name+"_data", str(id), "{}_desc.nt".format(id))
    if not folder:
        os.makedirs(folder_path)
    if not os.path.exists(os.path.join(folder_path, str(id))):
        os.makedirs(os.path.join(folder_path, str(id)))
    res_path = os.path.join(folder_path, str(id),"{}_top{}.nt".format(id, len(top_k)))
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

def get_res(name, k, m):
    '''

    :param name: "dbpedia" or "lmdb"
    :param k: number of cluster, hyperparameter
    :param m: the fuzzy k-means m
    :return:
    '''
    root = os.path.abspath(os.path.dirname(os.getcwd()))
    if name == "dbpedia":
        all_file = os.path.join(root, "data_analysis", "dbpedia", "dbpedia_all.txt")
        model_path = os.path.join(root,"embedding","model_dbpedia","dbpedia_transe_model","trained_model.pkl")
        file_base = os.path.join(root,"data_analysis", "dbpedia")
        file_path = []
        for i in range(1,101):
            file_path.append({os.path.join(file_base,"{}_desc.nt".format(i)):i})
        for i in range(141, 166):
            file_path.append({os.path.join(file_base,"{}_desc.nt".format(i)):i})

    elif name == "lmdb":
        all_file = os.path.join(root, "data_analysis", "lmdb", "lmdb_all.txt")
        model_path = os.path.join(root,"embedding","model_lmdb","lmdb_transe_model","trained_model.pkl")
        file_base = os.path.join(root,"data_analysis", "lmdb")
        file_path = []
        for i in range(101,141):
            file_path.append({os.path.join(file_base,"{}_desc.nt".format(i)):i})
        for i in range(166, 176):
            file_path.append({os.path.join(file_base,"{}_desc.nt".format(i)):i})


    model = torch.load(model_path)
    tf = TriplesFactory.from_path(all_file)
    for file in file_path:
        key = list(file)[0] # file path
        value = file[key] # id
        embedding_rep = get_embedding_representation(tf, model, key)
        t = FCM(embedding_rep, k, m, 0.001).forward()
        top_5 = greedy_search(t, 5)
        top_5.sort()
        store(top_5, key, value, k, m, name)
        top_10 = greedy_search(t, 10)
        top_10.sort()
        store(top_10, key, value, k, m, name)


