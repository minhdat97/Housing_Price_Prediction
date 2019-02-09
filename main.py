# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 17:15:32 2019

@author: TRANMINHDAT
"""

import pandas as pd
from IPython import get_ipython
#import matplotlib.pyplot as plt
#import seaborn as sns
#import numpy as np
#from scipy.stats import norm
#from sklearn.preprocessing import StandardScaler
#from scipy import stats
import warnings
warnings.filterwarnings('ignore')

def run():
    ipy = get_ipython()
    if ipy is not None:
        ipy.run_line_magic('matplotlib', 'inline')
    df_train = pd.read_csv('input/train.csv')
    
    print(df_train.columns)
    print(df_train['SalePrice'].describe())

def main():
    run()
    
if __name__ == '__main__':
    main()