# @Author : Cheng Huang
# @Time   : 18:56 2022/10/19
# @File   : check_multiple.py
import os
from rdflib import Graph

root = os.path.abspath(os.path.dirname(os.getcwd()))
print("==========dbpedia multi relation==========")
dblist = [i for i in range(1, 101)]
dblist += [i for i in range(141, 166)]
for i in dblist:
    multiedge_dict = {}
    path = os.path.join(root, "data/dbpedia_data/{}/{}_desc.nt".format(i, i))
    g = Graph()
    g.parse(path)
    print(i)
    for stmt in g:
        key = str(stmt[0]) +"--"+ str(stmt[2])
        if key not in multiedge_dict:
            multiedge_dict[key] = 1
        else:
            multiedge_dict[key] += 1
            if multiedge_dict[key] == 2:
                print(stmt[0], stmt[2])


print("==========lmdb multi relation==========")
lmlist = [i for i in range(101, 141)]
lmlist += [i for i in range(166, 176)]

for i in lmlist:
    multiedge_dict = {}
    path = os.path.join(root, "data/lmdb_data/{}/{}_desc.nt".format(i, i))
    g = Graph()
    g.parse(path)
    print(i)
    for stmt in g:
        key = str(stmt[0]) +"--"+ str(stmt[2])
        if key not in multiedge_dict:
            multiedge_dict[key] = 1
        else:
            multiedge_dict[key] += 1
            if multiedge_dict[key] == 2:
                print(stmt[0], stmt[2])
