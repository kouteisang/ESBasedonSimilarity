# @Author : Cheng Huang
# @Time   : 15:15 2022/9/26
# @File   : main.py
from experiment.write_result import get_res
from enum import Enum

class Data(Enum):
    DBPEDIA = "dbpedia"
    LMDB = "lmdb"

if __name__ == '__main__':
    '''
        :parameter1 : dataset DBPEDIA or LMDB
        :parameter2 : k(number of cluster)
        :parameter3 : m(fuzzy parameter)
    '''
    # get_res("lmdb", 5, 5)