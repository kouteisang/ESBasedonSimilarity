import os
from rdflib.graph import Graph
from rdflib.extras.external_graph_libs import rdflib_to_networkx_multidigraph
import networkx as nx
import pandas as pd
from networkx import ego_graph
from rdflib import URIRef
import pickle

#G is directed, should be converted to undirected to check the connectivity and number of components
path = os.path.dirname(os.path.realpath(__file__))
print(path)

def get_all_second_hop_entity(G):
  lmdbG=nx.MultiDiGraph()
  entitylist = pd.read_csv(path + '/data/elist.txt', sep='\t', index_col=0)
  for namekg in ['lmdb','dbpedia']:
    namekg_entity=entitylist[entitylist.dataset == namekg]
    for entity in namekg_entity['euri'][:5]:
      temp_ego=ego_graph(G,URIRef(entity),radius=2,undirected=True)
      # edges = temp_ego.edges()
      # for edge in edges:
      #   head = edge[0]
      #   tail = edge[1]
      #   rel = list(temp_ego.get_edge_data((edge[0]), (edge[1])).keys())[0]
      combinedkg=nx.compose(lmdbG,temp_ego)
    # nx.write_gml(combinedkg)
    nx.write_gpickle(combinedkg, path+"/data/datasets/Sample_second_"+str(namekg)+"_hop-KG.gpickle")

g=Graph()
g = g.parse(path+"/data/Cleaned_KG_line_Owl_thing_31_10.nt", format='nt')
G = rdflib_to_networkx_multidigraph(g)
get_all_second_hop_entity(G)

# G1=nx.MultiDiGraph()
# G1 = pickle.load(open(path+"/data/datasets/Sample_second_lmdb_hop-KG", 'rb'))
