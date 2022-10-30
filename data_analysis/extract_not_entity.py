# @Author : Cheng Huang
# @Time   : 19:27 2022/10/25
# @File   : extract_not_entity.py
import os
import pandas as pd
from rdflib import Graph

def get_entity_list(type):
    path = os.path.join(os.path.abspath(os.path.dirname(os.getcwd())), 'data', "elist.txt")
    euri = pd.read_csv(path, on_bad_lines='skip', sep='\t')['euri']
    if type == "dbpedia":
        entity_list = [str(entity) for entity in euri[:125]]
    elif type == "lmdb":
        entity_list = [str(entity) for entity in euri[125:]]
    return entity_list

def extract(type):
    entity_not_list= []
    entity_list = get_entity_list(type)
    if type == "dbpedia":
        index = [i for i in range(1, 101)]
        index += [i for i in range(141, 166)]
    elif type == 'lmdb':
        index = [i for i in range(101, 141)]
        index += [i for i in range(166, 176)]

    for i in index:
        path = os.path.join(os.path.abspath(os.path.dirname(os.getcwd())),'data','{}_data'.format(type),str(i),"{}_desc.nt".format(i))
        g = Graph()
        g.parse(path)
        for stmt in g:
            if str(stmt[0]) not in entity_list:
                entity_not_list.append(str(stmt[0]))
            if str(stmt[2]) not in entity_list:
                entity_not_list.append(str(stmt[2]))

    return entity_not_list

entity_not_list = extract("dbpedia")
for item in entity_not_list:
    if "yago" in item:
        print(item)