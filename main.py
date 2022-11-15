# @Author : Cheng Huang
# @Time   : 15:15 2022/9/26
# @File   : main.py
import os

from experiment.complete_result import get_complete_result
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

if __name__ == '__main__':
    '''
        :parameter1 : dataset DBPEDIA or LMDB
        :parameter2 : k(number of cluster)
        :parameter3 : m(fuzzy parameter)
    '''
    k = 10
    m = 5
    get_wrong_res("dbpedia", k, m, "transe")
    get_wrong_res("lmdb", k, m, "transe")





