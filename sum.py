# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 14:34:07 2019

@author: yam
"""
import pandas as pd

def sum(db):
    db['gain2'] =db['GAIN_DEBITS']+db['GAIN_CREDITS']
    return db[['gain2','GAIN_DEBITS','GAIN_CREDITS']]

def get_output_schema():
    return pd.DataFrame({
            'GAIN_DEBITS' : prep_decimal(),
            'GAIN_CREDITS' : prep_decimal(),
            'gain2' : prep_decimal()
            });