# @Author : Cheng Huang
# @Time   : 18:54 2022/11/1
# @File   : complete_result.py
import os

import torch
from pykeen.triples import TriplesFactory
from embedding.get_embedding import get_embedding_representation
from greedy.variance_search import cluster_variance
from greedy.wrong_experiment_search import wrong_cluster_entropy
from soft_clustering.fuzzy_k_means import FCM
from greedy.entropy_search import cluster_entropy



def store(top_k, type, id, k, m, name):
    root = os.path.abspath(os.path.dirname(os.getcwd()))+"/ESBasedonSimilarity/"
    folder_name = "wrong_complete_k_" + str(k) + "_m_" + str(m)
    folder_path = os.path.join(root, "res_data", folder_name, name)
    folder = os.path.exists(folder_path)
    if not folder:
        os.makedirs(folder_path)
    if not os.path.exists(os.path.join(folder_path, str(id))):
        os.makedirs(os.path.join(folder_path, str(id)))

    file_origin = os.path.join(root, "data", name+"_data", str(id), "{}_desc.nt".format(id))

    if type == "top":
        res_path = os.path.join(folder_path, str(id),"{}_top{}.nt".format(id, len(top_k)))
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

def get_wrong_complete_result(name, k, m, type):
    """

    :param name: "dbpedia" or "lmdb"
    :param k: number of cluster, hyperparameter
    :param m: the fuzzy k-means m
    :param type: embedding method transe or distmult
    :return:
    """
    root = os.path.abspath(os.path.dirname(os.getcwd())) + "/ESBasedonSimilarity/"
    if name == "lmdb":
        all_file = os.path.join(root, "complete_data", "lmdb", "complete_extract_lmdb.tsv")
        if type == "transe":
            model_path = os.path.join(root,"embedding","model_complete_lmdb","lmdb_transe_model","trained_model.pkl")

        file_base = os.path.join(root,"data_analysis", "lmdb")
        file_path = []
        for i in range(101,141):
            file_path.append({os.path.join(file_base,"{}_desc.nt".format(i)):i})
        for i in range(166, 176):
            file_path.append({os.path.join(file_base,"{}_desc.nt".format(i)):i})

    if name == "dbpedia":
        all_file = os.path.join(root, "complete_data", "dbpedia", "complete_extract_dbpedia.tsv")
        if type == "transe":
            model_path = os.path.join(root,"embedding","model_complete_dbpedia","dbpedia_transe_model","trained_model.pkl")

        file_base = os.path.join(root,"data_analysis", "dbpedia")
        file_path = []
        for i in range(1,101):
            file_path.append({os.path.join(file_base,"{}_desc.nt".format(i)):i})
        for i in range(141, 166):
            file_path.append({os.path.join(file_base,"{}_desc.nt".format(i)):i})

    model = torch.load(model_path)
    tf = TriplesFactory.from_path(all_file)

    for file in file_path:
        key = list(file)[0]  # file path
        value = file[key]  # id
        embedding_rep = get_embedding_representation(tf, model, key)
        t = FCM(embedding_rep, k, m, 0.001).forward()
        res = wrong_cluster_entropy(t, key)  # entropy based method
        top_5 = res[:5]
        top_5.sort()
        store(top_5, "top", value, k, m, name)
        top_10 = res[:10]
        top_10.sort()
        store(top_10, "top", value, k, m, name)
        store(res, "rank", value, k, m, name)
