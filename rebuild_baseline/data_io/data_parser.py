# -*- coding: utf-8 -*-
'''貌似是根据tensorflow的数据集，一行一行得处理数据'''

import numpy as np
import tensorflow as tf

class PosShifts(object):
    '''shift代表每个特征的总个数，通过shift将所有特征合并为一个特征'''
    _shifts = []
    def __init__(self):
        PosShifts._shifts = [73974,396,4122689,850308,461, 5]
    
    @staticmethod
    def get_features_num():
        return sum(PosShifts._shifts)
    
    @staticmethod
    def shift():
        shifts = PosShifts._shifts
        shifts = [0]+shifts
        shifts = [sum(shifts[:(i+1)]) for i in range(len(shifts))]
        return shifts

class DataParser(object):
    
    @staticmethod
    def data_parser(line, label_index):
        content = line.split(',')
        label = np.float32(content[label_index].strip())
        feature_num = 5
        features = content[:feature_num+1]
        features = map(lambda x:np.float32(x), features)
        idx = [0 if feature<0 else  feature for feature in features]
        features = [np.float32(0) if feature<0 else np.float32(1) for feature in features]
        features = features[:feature_num]
        
        idx = idx[:feature_num]
        
        shifts = PosShifts.shift()
        idx = [idx[i]+shifts[i] for i in range(len(idx))]
        idx = map(lambda x : np.int32(x) , idx)
        
        return idx, features, label

class LineParser(object):
    
    @staticmethod
    def parse_finish_line(line):
        
        return tf.py_func(DataParser.data_parser, [line, 6], [tf.int32, tf.float32, tf.float32])
    
    @staticmethod
    def parse_like_line(line):
        
        return tf.py_func(DataParser.data_parser, [line, 7], [tf.int32, tf.float32, tf.float32])
 
                 
    
