# -*- coding: utf-8 -*-
''' 通用的参数设置'''
import argparse

def init_model_args():
    
    parser = argparse.ArgumentParser()
    #training_size
    parser.add_argument('--batch_size', type=int, default=40)
    parser.add_argument('--embedding_size', type=int, default=40)
    parser.add_argument('--num_epochs', type=int, default=200)
    
    #optimize:学习速率，优化器
    parser.add_argument('--optimizer', default='adam', choices=['adam', 'adagrad'])
    parser.add_argument('--lr', type=float, default=0.001)
    
    #数据保存路径
    parser.add_argument('--save_model_dir', default='save_model')
    parser.add_argument('--training_path', required=True)
    parser.add_argument('--validation_path', required=True)
    
    #选择任务总类，finish或是like
    parser.add_argument('--task', default='finish')
    
    #track默认就是2了，数据问题
    
    args = parser.parse_args()
    return args