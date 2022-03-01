import pandas as pd
import re
import os
from typing import List

PATH = 'utils/datasets/Time_Series_Datasets/data/'

def get_filenames() -> List[str]:
    ''' Get filenames '''

    filenames = []
    for _, _, files in os.walk(PATH, topdown=False):
        for name in files:
            filenames.append(re.sub('.csv','',name))
    return filenames


def get_dataset(filename:object=None) -> pd.Series:
    ''' Get a dataset

    Params
    ------
        filename: object (string or int) (default is None)
            The dataset to return. If None, prints a list of available datasets
            Can also choose dataset by index

    '''

    filenames = get_filenames()

    if type(filename) == int and filename <= len(filenames) and filename > 0:
        filename = filenames[filename-1]
    
    elif filename not in filenames:
        options = [str(i+1)+':\t'+f for i,f in enumerate(filenames)]
        print(
            'Files can be chosen from: \n' + '\n'.join(options)
        )
        return None
    
    return pd.read_csv(PATH+filename+'.csv')