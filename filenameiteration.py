# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 21:46:49 2023

@author: julsi
"""


import os


    
path = 'C:/Users/'
i = 0
for filename in os.listdir(path):
    os.rename(os.path.join(path,filename), os.path.join(path,'map_'+str(1261+i)+'.fits'))
    i = i +1