# @Author : Cheng Huang
# @Time   : 15:15 2022/9/26
# @File   : main.py
import os

from experiment.complete_result import get_complete_result
from experiment.random_result import random_generate
from experiment.remove_global_complete import remove_list_complete
from experiment.remove_global_esbm import remove_list_esbm
from experiment.write_result import get_res
import argparse


# def parse_args():
#     args = argparse.ArgumentParser()
#     args.add_argument('-name', '--name', type=str, default='dbpedia', help='File name(dbpedia or lmdb)')
#     args.add_argument('-k', '--k', type=int, default=5, help="Number of cluster")
#     args.add_argument('-m', '--m', type=int, default=5, help='Fuzzy parameter')
#     args = args.parse_args()
#     return args
#
# args = parse_args()
#
# get_res(args.name, args.k, args.m)
from experiment.wrong_experiment import get_wrong_res
from experiment.wrong_experiment_complete import get_wrong_complete_result

#
# subprocess.run(["java", "-jar" ,"/Users/huangcheng/Documents/ESBasedonSimilarity/res_data/esummeval_v1.2.jar"
#                 ,"/Users/huangcheng/Documents/ESBasedonSimilarity/ESBM_benchmark_v1.2"
#                 ,"/Users/huangcheng/Documents/ESBasedonSimilarity/global_res/complete_remove_top2/global_reomove_complete_k_8_m_9"])

if __name__ == '__main__':
    '''
        :parameter1 : dataset DBPEDIA or LMDB
        :parameter2 : k(number of cluster)
        :parameter3 : m(fuzzy parameter)
    '''
    # k = 3
    # m = 2
    for i in range(50):
        random_generate("dbpedia", i)
        random_generate("lmdb", i)






