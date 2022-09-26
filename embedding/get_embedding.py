# @Author : Cheng Huang
# @Time   : 10:37 2022/9/19
# @File   : get_embedding.py
import os
import numpy as np
from typing import List

import torch
from pykeen.triples import TriplesFactory



def get_embedding_representation(tf, model, file_path):
    '''
    Args:
        tf: triple factory
        model: model
        file_path(str): file need to get the embedding

    Returns:
        emb_rep(list): return embedding representation
    '''
    emb_rep = []
    entity_embedding = model.entity_representations[0](indices=None).detach().numpy()
    relation_embedding = model.relation_representations[0](indices=None).detach().numpy()
    with open(file_path, 'r') as f:
        for line in f:
            h, r, t = line.split("\t")
            t = t.rstrip("\n")
            # get the corresponding id
            h, t = tf.entities_to_ids([h, t])
            r = tf.relations_to_ids([r])[0]
            # get the embedding
            h = entity_embedding[h].tolist()
            t = entity_embedding[t].tolist()
            r = relation_embedding[r].tolist()
            emb_rep.append(r+t)

    return emb_rep


if __name__ == '__main__':
    # for test
    root = os.path.abspath(os.path.dirname(os.getcwd()))
    lm_path = os.path.join(root, "data_analysis", "lmdb", "lmdb_all.txt")
    tf = TriplesFactory.from_path(lm_path)

    model = torch.load("/Users/huangcheng/Documents/ESBasedonSimilarity/embedding/model_lmdb/lmdb_transe_model/trained_model.pkl")

    file_path = "/Users/huangcheng/Documents/ESBasedonSimilarity/data_analysis/lmdb/101_desc.nt"

    res = get_embedding_representation(tf, model, file_path)

