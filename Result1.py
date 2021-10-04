# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 13:41:23 2021

@author: BektasBaysal
"""

from datetime import datetime

def listConcatenate(*args):
    start = datetime.now()
    a = list()
    for i in args:
      a +=i 
    print(a)
    end= datetime.now()
    print(end-start)
    return a
listConcatenate([1, 2, 3, 7, 10], [1, 3, 5], [1, 2, 3], [1.5, 7.6], ["a", "word"] )


