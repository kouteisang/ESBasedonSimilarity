# @Author : Cheng Huang
# @Time   : 20:17 2022/11/1
# @File   : tt.py

'http://dbpedia.org/ontology/programmeFormat'
import torch
from pykeen.triples import TriplesFactory

# model = torch.load("/Users/huangcheng/Documents/ESBasedonSimilarity/embedding/model_complete_dbpedia/dbpedia_transe_model")
# model.entity_representations[0](indices=None).detach().numpy()
#
# tf = TriplesFactory.from_path("/Users/huangcheng/Documents/ESBasedonSimilarity/complete_data/dbpedia/complete_dbpedia.tsv")
#
# ids = tf.relations_to_ids(["http://dbpedia.org/ontology/programmeFormat"])[0]
# print(ids)

cnt = 0
remove = set()
new_complete = open("/complete_data/dbpedia/complete_dbpedia.tsv", 'w')
with open("/Users/huangcheng/Documents/ESBasedonSimilarity/complete_data/dbpedia/complete_dbpedia.tsv", 'r') as f:
    for line in f:
        if line in remove:
            print(line)
            continue
        else:
            remove.add(line)
            new_complete.write(line)
            cnt = cnt + 1
print(cnt)