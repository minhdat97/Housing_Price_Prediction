# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 17:15:32 2019

@author: TRANMINHDAT
"""

import pandas as pd
#import matplotlib.pyplot as plt
#import seaborn as sns
#import numpy as np
#from scipy.stats import norm
#from sklearn.preprocessing import StandardScaler
#from scipy import stats
import warnings
warnings.filterwarnings('ignore')

def run():
    df_train = pd.read_csv('./input/train.csv')
    df_train.columns

def main():
    run()
    
if __name__ == '__main__':
    main()