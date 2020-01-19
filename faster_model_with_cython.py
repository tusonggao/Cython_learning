# https://github.com/huggingface/100-times-faster-nlp
from __future__ import print_function, division, with_statement
import os
import sys
import time
import numpy as np
import pandas as pd
import timeit
from c1 import great_circle

'''
from cymem.cymem cimport Pool
from random import random

cdef struct Rectangle:
    float w
    float h

cdef int check_rectangles(Rectangle* rectangles, int n_rectangles, float threshold):
    cdef int n_out = 0
    # C arrays contain no size information => we need to give it explicitly
    for rectangle in rectangles[:n_rectangles]:
        if rectangle[i].w * rectangle[i].h > threshold:
            n_out += 1
    return n_out

def main():
    cdef:
        int n_rectangles = 10000000
        float threshold = 0.25
        Pool mem = Pool()
        Rectangle* rectangles = <Rectangle*>mem.alloc(n_rectangles, sizeof(Rectangle))
    for i in range(n_rectangles):
        rectangles[i].w = random()
        rectangles[i].h = random()
    n_out = check_rectangles(rectangles, n_rectangles, threshold)
    print(n_out)
'''

num=10#表示运行多少次
# t = timeit.Timer("c1.great_circle(%f,%f,%f,%f)" % (lon1,lat1,lon2,lat2),"import c1")
t = timeit.Timer("c1.great_circle(%f,%f,%f,%f)" % (16,124,76,173),"import c1")
print("Cython function (still using python math)", t.timeit(num), "sec")

if __name__=='__main__':
    pass
    #main()
    
