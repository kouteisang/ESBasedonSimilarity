# @Author : Cheng Huang
# @Time   : 11:04 2022/10/10
# @File   : relation_percentage.py
import os
import numpy as np
import matplotlib.pyplot as plt


def generate_relation_percentage(path):
    if "dbpedia" in path:
        index = [i for i in range(1, 101)]
        index += [i for i in range(141, 166)]
        drp = open(os.path.join(path, 'dbpedia_relation_percentage.txt'), 'w')
    elif "lmdb" in path:
        index = [i for i in range(101, 141)]
        index += [i for i in range(166, 176)]
        drp = open(os.path.join(path, 'lmdb_relation_percentage.txt'), 'w')

    count = 0
    for i in index:
        rel_count = {}
        desc = os.path.join(path, '{}_desc.nt'.format(i))
        with open(desc, 'r') as f:
            for line in f:
                rel = line.split("\t")[1]
                if rel not in rel_count:
                    rel_count[rel] = 1
                else:
                    rel_count[rel] = rel_count[rel] + 1
        f.close()
        rel_count = sorted(rel_count.items(), key = lambda item:item[1], reverse=True)
        per_count = [x[1] for x in rel_count]
        labels = [x[0] for x in rel_count]
        percentage = np.array(per_count)/sum(per_count)
        if percentage[0] > 0.4:
            count += 1
        # plt.title("{}_desc".format(i))
        # plt.pie(percentage, labels=labels,autopct='%.2f%%')
        # plt.savefig("./dbpedia_rel_image/{}_desc.jpg".format(i))
        percentage_map = list(zip(labels,percentage))
    #     drp.write("{}_desc\n".format(i))
    #     drp.write(str(rel_count))
    #     drp.write("\n")
    #     drp.write(str(percentage_map))
    #     drp.write("\n")
    #     drp.write("\n")
    # drp.close()
    print(count)

if __name__ == '__main__':
    root = os.getcwd()
    dbpedia_path = os.path.join(root, "dbpedia")
    lmdb_path = os.path.join(root, "lmdb")
    generate_relation_percentage(dbpedia_path)
    generate_relation_percentage(lmdb_path)
