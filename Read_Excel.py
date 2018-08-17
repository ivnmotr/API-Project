# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 22:12:34 2018

@author: Ivan
"""

import pandas as pd

def getData(url):
    # Read excel file in desktop
    df = pd.read_excel(url, sheet_name=0)
    # Transform MPN column into a list
    mpn = df['MPN'].tolist()
    # return list of mpn
    return mpn