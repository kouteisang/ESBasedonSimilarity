# @Author : Cheng Huang
# @Time   : 18:54 2022/10/27
# @File   : count_each_entity.py
import os


def count_entity_length(type):
    root = os.path.abspath(os.path.dirname(os.getcwd()))
    if type == "dbpedia":
        index = [i for i in range(1, 101)]
        index += [i for i in range(141, 166)]
        esbm_length = []
        for i in index:
            with open(os.path.join(root, "data", "dbpedia_data", str(i), "{}_desc.nt".format(i))) as f:
                cnt = 0
                for line in f:
                    cnt = cnt + 1
                esbm_length.append(cnt)
        print(esbm_length)

count_entity_length("dbpedia")